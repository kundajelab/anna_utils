import MOODS.parsers
import MOODS.tools
import MOODS.scan
import pysam
import argparse
import pdb

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
    parser.add_argument('--pseudocount',type=float,help="pseudocount to add when providing a matrix of frequency values rather than a PWM",default=1e-4)
    return parser.parse_args()


def main():
    args=parse_args()    
    reference = pysam.FastaFile(args.reference)
    bg=parse_background_freqs(args.background_freqs)
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
    positions=[i.split('\t') for i in open(args.positions_bed,'r').read().strip().replace(":","\t").replace("-","\t").split('\n')]
    for position in positions:
        seq=reference.fetch(position[0],int(position[1]),int(position[2]))
        results=scanner.scan(seq)
        pdb.set_trace()
        
if __name__=="__main__":
    main()
    
