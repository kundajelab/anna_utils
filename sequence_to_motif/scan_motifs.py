#script that utilizes MOODS python library to scan 1kb sequences from hg19 with HOCOMOCO motifs
import math 
import argparse
import pysam
import os 
import numpy as np 
import MOODS.parsers
import MOODS.tools
import MOODS.scan
from itertools import izip
import h5py 
import pdb 

def parse_args():
    parser=argparse.ArgumentParser(description='provide a director of PWM motif files and source fasta file as well the interval sizes to scan')
    parser.add_argument('--pwm_list',help='file containing list of directories to all pwms to use, see example pwm_list_cisbp.txt in this repository')
    parser.add_argument('--reference',help='reference fasta file')
    parser.add_argument('--out_prefix',help='output file prefix')
    parser.add_argument('--chrom_sizes',help='file containing sizes of chromosomes')
    parser.add_argument('--background_freqs',help='file containing the background allele frequencies',default=None)
    parser.add_argument('--p_val',type=float,help='p-value threshold for inferring motif presence in a sequence',default=0.001)
    parser.add_argument('--reference_bin_size',type=int,help='bin sizes for scanning reference genome',default=1000)
    parser.add_argument('--num_hits_per_motif',type=int,help="maximum instances of a single motif in a sequence that will be recorded",default=1)
    parser.add_argument('--chrom',help="optionally, specify the chromosomes of interest for the parser to focus on, comma-separated list of chromosomes",default=None)
    parser.add_argument('--positions_bed',help="input bed file containing sequence positions to scan",default=None)
    parser.add_argument('--binarize',help="remove this flag if you don't want to binarize the scores",action='store_true')
    parser.add_argument('--dump_hdf5',help="add this flag if you want the data matrix to be stored in an hdf5 format compatible with momma_dragonn",action='store_true')
    parser.add_argument('--labels_for_hdf5',help="filename containing the labels file to use for \"y\" when storing the output in hdf5 compatible with momma_dragonn")
    parser.add_argument('--numlabels_for_hdf5',type=int,help="number of labels present in associated labels file") 
    parser.add_argument('--thresholds',help="file containing motif name to threshold mapping")
    parser.add_argument('--position_bin_size',type=int,help="bin size for scanning the positions file, if we want to record positional information",default=None)
    parser.add_argument('--freqs',help="use this flag if you are providing a matrix of frequencies rather than a PWM",action='store_true')
    parser.add_argument('--totext',help="store results in a text file of motif to scores",action='store_true')
    parser.add_argument('--pseudocount',type=float,help="pseudocount to add when providing a matrix of frequency values rather than a PWM",default=1e-4)
    return parser.parse_args()

#helper function to convert numpy array to tuple (MOODS needs tuples for scanning)
def totuple(a):
    try:
        return tuple(totuple(i) for i in a)
    except TypeError:
        return a
    
def parse_chrom_sizes(chrom_sizes_file):
    chrom_sizes=dict()
    with open(chrom_sizes_file) as f:
        data=f.read().strip().split('\n')
        for line in data:
            tokens=line.split('\t')
            chrom_sizes[tokens[0]]=int(tokens[1])
    return chrom_sizes 

def calculate_bg_from_scratch(reference,positions_bed_file):
    bg_freqs=[0,0,0,0]
    numbases=0
    positions_bed=open(positions_bed_file,'r').read().strip().replace(':','\t').replace('-','\t').split('\n')
    positions_bed=[entry.split('\t') for entry in positions_bed]
    for region in positions_bed:
        seq=(reference.fetch(region[0],int(region[1]),int(region[2]))).lower()
        numA=seq.count('a')
        numC=seq.count('c')
        numG=seq.count('g') 
        numT=seq.count('t') 
        numbases=numbases+numA+numC+numG+numT
        bg_freqs[0]+=numA
        bg_freqs[1]+=numC
        bg_freqs[2]+=numG
        bg_freqs[3]+=numT
    bg_freqs=[float(i)/numbases for i in bg_freqs]
    print(str(bg_freqs))
    return bg_freqs

def parse_background_freqs(background_freqs_file):
    data=open(background_freqs_file,'r').read().strip().split('\n')
    bg_freqs=[0,0,0,0]
    for line in data:
        tokens=line.split('\t')
        if tokens[0]=="A":
            bg_freqs[0]=float(tokens[1])
        elif tokens[0]=="C":
            bg_freqs[1]=float(tokens[1])
        elif tokens[0]=="G":
            bg_freqs[2]=float(tokens[1])
        elif tokens[0]=="T":
            bg_freqs[3]=float(tokens[1])
    print str(bg_freqs)
    return tuple(bg_freqs) 


def bin_motif_hits(bins_cur_motif,results_cur_motif,num_hits_per_motif):
    hit_dict=dict()
    for i in range(len(bins_cur_motif)):
        cur_bin=bins_cur_motif[i]
        cur_score=results_cur_motif[i]
        if cur_bin not in hit_dict:
            hit_dict[cur_bin]=[cur_score]
        else:
            hit_dict[cur_bin].append(cur_score)
    for bin in hit_dict:
        hit_dict[bin].sort(reverse=True)
        hit_dict[bin]=hit_dict[bin]+[0]*(num_hits_per_motif-len(hit_dict[bin]))
        hit_dict[bin]=hit_dict[bin][0:num_hits_per_motif]
    #print(str(hit_dict))
    return hit_dict 

def global_scan(args,chrom_sizes,num_motifs,scanner,thresholds,reference,motif_names,output_dir):         
    #iterate through each chromosome in the reference sequence to scan for motifs
    if args.chrom==None:
        chroms=chrom_sizes.keys()
    else:
        chroms=args.chrom.split(',')
    for chrom in chroms:
        print("scanning:"+str(chrom))
        #pre-allocate the output numpy array with zeros
        num_sequence_bins=chrom_sizes[chrom]/args.bin_size
        chrom_motif_mat=np.zeros((num_sequence_bins,args.num_hits_per_motif*num_motifs))
        chrom_pos_mat=np.zeros((num_sequence_bins,2))
        
        pos_start=0
        pos_end=pos_start+args.bin_size
        bin_index=0 
        while pos_end < chrom_sizes[chrom]:
            if pos_start%1000000==0: 
                print("pos_start:"+str(pos_start)+"/"+str(chrom_sizes[chrom])) 
            #get the next genome bin to scan 
            seq=reference.fetch(chrom,pos_start,pos_end)
            #scan!
            results=scanner.scan(seq)
            #threshold the motif scores to binary values, either take the max score or the top 3 scores to threshold 
            for motif_index in range(num_motifs):
                #get the top n scores for each motif
                results_cur_motif=[r.score for r in results[motif_index]]
                results_cur_motif.sort(reverse=True)
                #pad to the desired length
                results_cur_motif+=[0]*(args.num_hits_per_motif-len(results_cur_motif))
                #truncate to the desired length
                results_cur_motif=results_cur_motif[0:args.num_hits_per_motif]
                if args.binarize==False:
                    chrom_motif_mat[bin_index,motif_index*args.num_hits_per_motif:(motif_index+1)*args.num_hits_per_motif]=results_cur_motif
                else:
                    chrom_motif_mat[bin_index,motif_index*args.num_hits_per_motif:(motif_index+1)*args.num_hits_per_motif]=[int(m>thresholds[motif_index])for m in results_cur_motif]
            chrom_pos_mat[bin_index][0]=pos_start
            chrom_pos_mat[bin_index][1]=pos_end                                 
            #update indices 
            pos_start=pos_end
            pos_end=pos_start+args.bin_size
            bin_index+=1

        #save output numpy pickles for the chromosome
        np.save("/".join([output_dir,".".join([chrom,"mat"])]),chrom_motif_mat)
        np.save("/".join([output_dir,".".join([chrom,"pos"])]),chrom_pos_mat)
        outf_names=open(output_dir+'/motif_names.txt','w')
        outf_names.write('\n'.join(motif_names))
        print("finished processing chromosome:"+str(chrom))
        
def scan_specified_positions(args,positions,num_motifs,scanner,thresholds,reference,motif_names,output_dir):
    num_peaks=len(positions)
    try:
        seq_length=int(positions[0][2])-int(positions[0][1])
    except:
        pdb.set_trace() 
    #handle case when we want to encode positional info!
    if args.position_bin_size!=None:
        #figure out how many bins needed to parse full sequence
        if seq_length%args.position_bin_size!=0:
            raise Exception("position_bin_size argument must be an exact factor of the sequence length!"+
                            "You have provided a sequence of length:"+
                            str(seq_length)+
                            ", but the position_bin_size argument is:"+
                            str(args.position_bin_size))
        num_bins_per_sequence=seq_length/args.position_bin_size
        position_bin_size=args.position_bin_size
    else:
        num_bins_per_sequence=1
        position_bin_size=seq_length
    print("num_bins_per_sequence:"+str(num_bins_per_sequence))
    print("positin_bin_size:"+str(position_bin_size))


    if args.dump_hdf5==True:
        print("creating output hdf5 file!!") 
        labels_for_hdf5=np.loadtxt(args.labels_for_hdf5,skiprows=1,usecols=range(1,args.numlabels_for_hdf5+1),dtype=int)
        label_pos=np.loadtxt(args.labels_for_hdf5,skiprows=1,usecols=range(0,1),dtype=object)
        num_tasks=args.numlabels_for_hdf5
        label_positions=dict()
        for i in range(label_pos.shape[0]):
            label_positions[label_pos[i]]=labels_for_hdf5[i]
        print("read in labels for hdf5")
        label_mat=np.zeros((num_peaks,num_tasks))
        for i in range(len(positions)):
            label_entry="_".join(positions[i])
            label_mat[i]=label_positions[label_entry]

        outf=h5py.File(args.out_prefix+".hdf5",'w')
        motif_mat=outf.create_dataset("X/sequence",data=np.zeros((num_peaks,args.num_hits_per_motif*num_motifs*num_bins_per_sequence)),chunks=True)
        out_labels=outf.create_dataset("Y/output",data=label_mat,chunks=True)
        print("wrote labels to hdf5")
    else:
        motif_mat=np.zeros((num_peaks,args.num_hits_per_motif*num_motifs*num_bins_per_sequence))
    peak_index=0 
    for position in positions:
        #scan!
        if peak_index%100==0:
            print(str(peak_index)+"/"+str(num_peaks))
        print(str(position))
        seq=reference.fetch(position[0],int(position[1]),int(position[2]))
        if len(position)>3:
            #add the mutation!
            varpos=int(math.ceil(len(seq)/2.0)-1)
            endpos=len(seq)
            seq=seq[0:varpos]+position[3]+seq[varpos+1:endpos]
        #print(str(seq))
        results=scanner.scan(seq)
        #print("results:"+str(results))
        for motif_index in range(num_motifs):
            results_cur_motif=[r.score for r in results[motif_index]]
            bins_cur_motif=[r.pos/position_bin_size for r in results[motif_index]]
            #get a dictionary of bins to scores
            score_dict=bin_motif_hits(bins_cur_motif,results_cur_motif,args.num_hits_per_motif)
            for cur_bin in score_dict:
                insert_start=motif_index*args.num_hits_per_motif*num_bins_per_sequence+(args.num_hits_per_motif*cur_bin)
                insert_end=motif_index*args.num_hits_per_motif*num_bins_per_sequence+(args.num_hits_per_motif*(cur_bin+1))
                #print(str(insert_start)+":"+str(insert_end))
                if args.binarize==False:
                    motif_mat[peak_index,insert_start:insert_end]=score_dict[cur_bin]
                else:
                    motif_mat[peak_index,insert_start:insert_end]=[int(m>thresholds[motif_index])for m in score_dict[cur_bin]]
        peak_index+=1
        
    if args.dump_hdf5==True:
        print("closing hdf5") 
        outf.flush()
        outf.close()
    elif args.totext==True:
        outf=open(output_dir+"/"+"motif_hits.txt",'w')
        outf.write("Chrom\tPeakStart\tPeakEnd\t"+'\t'.join(motif_names)+'\n')
        numrows=motif_mat.shape[0]
        for r in range(numrows):
            outf.write('\t'.join(positions[r])+'\t'+'\t'.join([str(i) for i in motif_mat[r,:]])+'\n')
    else:
        print("saving output numpy arrays") 
        #save the output numpy pickle
        #save output numpy pickles for the chromosome
        np.save("/".join([output_dir,"mat"]),motif_mat)
        #np.save("/".join([output_dir,"pos"]),pos_mat)
        outf_names=open(output_dir+'/motif_names.txt','w')
        outf_names.write('\n'.join(motif_names))
        
def get_thresholds(args,matrices,bg,motif_names):
    #check to see if the user provided a file of thresholds:
    if args.thresholds!=None:
        threshold_data=open(args.thresholds,'r').read().strip().split('\n')
        threshold_dict=dict()
        for line in threshold_data[1::]:
            tokens=line.split('\t')
            threshold_dict[tokens[0]]=float(tokens[3])
        thresholds=[threshold_dict[m.split('/')[-1]] for m in motif_names]
        #fill in any infinity values (i.e. no acceptable fdr for the motif found, in
        #that case we use the default MOODS value
        for i in range(len(motif_names)):
            if thresholds[i]==float("inf"):
                thresholds[i]=MOODS.tools.threshold_from_p(matrices[i],bg,args.p_val)
    else:
        thresholds=[MOODS.tools.threshold_from_p(m,bg,args.p_val) for m in matrices]
    return thresholds 

def main():
    args=parse_args()
    chrom_sizes=parse_chrom_sizes(args.chrom_sizes)
    print("parsed chromosome sizes")


    #prep the reference fasta
    reference=pysam.FastaFile(args.reference)

    if args.background_freqs!=None:
        bg = parse_background_freqs(args.background_freqs)
    else:
        print("No background_freqs argument provided, computing frequencies from positions_bed argument") 
        bg = calculate_bg_from_scratch(reference,args.positions_bed)
    print("got background frequencies")


    #get the matrix files
    matrix_file_names=open(args.pwm_list,'r').read().strip().split('\n') 
    matrices=[]
    motif_names=[matrix_file_name for matrix_file_name in matrix_file_names]
    for matrix_file_name in matrix_file_names:
        if args.freqs==False:
            #input matrices are in pwm format
            matrices.append(totuple(np.transpose(np.loadtxt(matrix_file_name,skiprows=1))))
        else:
            #input matrices are provided as frequency tables
            matrices.append(MOODS.parsers.pfm_to_log_odds(matrix_file_name,bg,args.pseudocount))

    #parse the pwm matrices 
    num_motifs=len(matrices)
    
    #get the p-value cutoff thresholds
    thresholds=get_thresholds(args,matrices,bg,motif_names)
    #create the moods scanner
    scanner = MOODS.scan.Scanner(7)
    scanner.set_motifs(matrices, bg, thresholds, )
    print('read in motif matrices and thresholds')

    #create the output s_m, s_3m, s_tf directories
    output_dir=args.out_prefix+"_"+str(args.num_hits_per_motif)+"_"+str(args.p_val)
    try:
        os.makedirs(output_dir)
    except:
        print("Directory already exists:"+output_dir) 
        
    #decide whether we are scanning globally or at specific positions from a bed file 
    if args.positions_bed==None:
        global_scan(args,chrom_sizes,num_motifs,scanner,thresholds,reference,motif_names,output_dir)
    else:
        positions=[i.split('\t') for i in open(args.positions_bed,'r').read().strip().replace(":","\t").replace("-","\t").split('\n')]
        scan_specified_positions(args,positions,num_motifs,scanner,thresholds,reference,motif_names,output_dir)


if __name__=='__main__':
    main()
    
