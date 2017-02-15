#performs the permutation test at a global level rather than for each hit region independently
import argparse
import pysam
import numpy as np
import MOODS.parsers
import MOODS.tools
import MOODS.scan
import random
import itertools
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


#helper function to convert numpy array to tuple (MOODS needs tuples for scanning)
def totuple(a):
    try:
        return tuple(totuple(i) for i in a)
    except TypeError:
        return a

def parse_args():
    parser=argparse.ArgumentParser(description='permutation test for a specified motif, globally')
    parser.add_argument("--foreground_bed",help="bed file containing the foreground region")
    parser.add_argument("--reference",help="reference fasta file")
    parser.add_argument("--out_prefix",help="output file prefix")
    parser.add_argument("--permuted_reference",help="permuted genome in bins of 1kb")
    parser.add_argument("--pwm",help="pwm file for motif of interest")
    parser.add_argument("--p_val",help="p-value cutoff for motif calling")
    parser.add_argument('--foreground_freqs',help='file containing the background allele frequencies,will be computed on the fly if not provided')
    return parser.parse_args() 

#parses the provided foreground bed file
def parse_foreground(foreground_file):
    foreground=open(foreground_file,'r').read().strip().split('\n')
    foreground=[entry.split('\t') for entry in foreground]
    return foreground

#compute the A,C,T,G content of the foreground 
def compute_base_freqs(reference,foreground,out_prefix):
    frequencies=[0,0,0,0]
    numbases=0
    for region in foreground:
        seq=(reference.fetch(region[0],int(region[1]),int(region[2]))).lower()
        numA=seq.count('a')
        numC=seq.count('c')
        numG=seq.count('g') 
        numT=seq.count('t') 
        numbases=numbases+numA+numC+numG+numT
        frequencies[0]+=numA
        frequencies[1]+=numC
        frequencies[2]+=numG
        frequencies[3]+=numT
    frequencies=[float(i)/numbases for i in frequencies]
    outf=open(out_prefix+".foreground_freqs.txt",'w')
    outf.write('\t'.join([str(i) for i in frequencies]))
    print("computed foreground!") 
    return frequencies

def update_distribution(distribution,new_entry):
    for score in new_entry:
        if score not in distribution:
            distribution[score]=1
        else:
            distribution[score]+=1
    return distribution 

def main():
    #read in the arguments 
    args=parse_args()

    #initialize the reference sequences
    reference=pysam.FastaFile(args.reference)
    permuted_reference=pysam.FastaFile(args.permuted_reference) 
    print("opened references") 

    #load the pwm 
    matrix_file_name=args.pwm
    matrix=totuple(np.transpose(np.loadtxt(matrix_file_name,skiprows=1)))
    motif_name=matrix_file_name.split('.')[0]
    print("read in motif of interest:"+str(motif_name))

    #read in the foreground & compute base frequencies 
    foreground=parse_foreground(args.foreground_bed)
    if args.foreground_freqs==None:
        fg_freqs=compute_base_freqs(reference,foreground,args.out_prefix)
    else:
        fg_freqs=[float(i) for i in open(args.foreground_freqs,'r').read().strip().split('\t')]
    print('computed base frequencies in foreground')

    threshold=MOODS.tools.threshold_from_p(matrix,fg_freqs,float(args.p_val))
    #initalize the MOODS scanner 
    scanner = MOODS.scan.Scanner(7)
    scanner.set_motifs([matrix], fg_freqs, [threshold],)
    print("initialized scanner...")
    
    #perform scan of original foreground, get histogram of hit scores
    distribution_original=dict()
    distribution_permuted=dict()
    list_original=[]
    list_permuted=[] 
    num_hits_original=0
    num_hits_permuted=0

    #scan each original & permuted region in the foreground
    num_entries=str(len(foreground))
    parsed=0 
    for entry in foreground:
        seq=reference.fetch(entry[0],int(entry[1]),int(entry[2]))
        seq_permuted=permuted_reference.fetch(entry[0],int(entry[1]),int(entry[2]))

        #update the distributions of motif hit scores 
        hits_original=scanner.scan(seq)[0]
        scores_original=[round(hit.score,2) for hit in hits_original]
        num_hits_original+=len(scores_original)
        #list_original[0:0]=scores_original 
        distribution_original=update_distribution(distribution_original,scores_original)
        
        hits_permuted=scanner.scan(seq_permuted)[0]
        scores_permuted=[hit.score for hit in hits_permuted]
        num_hits_permuted+=len(scores_permuted)
        #list_permuted[0:0]=scores_permuted 
        distribution_permuted=update_distribution(distribution_permuted,scores_permuted) 
        parsed+=1
        if parsed%1000==0:
            print str(parsed)+"/"+num_entries 
    print("completed scanning")
    
    #write out the histograms 
    outf_original=open(args.out_prefix+".original",'w')
    score_keys_original=distribution_original.keys()
    score_keys_original.sort()
    for key in score_keys_original:
        outf_original.write(str(key)+'\t'+str(distribution_original[key])+'\n')
        
    outf_permuted=open(args.out_prefix+".permuted",'w')
    score_keys_permuted=distribution_permuted.keys()
    score_keys_permuted.sort() 
    for key in score_keys_permuted:
        outf_permuted.write(str(key)+'\t'+str(distribution_permuted[key])+'\n')

    #plot!
    print("generating lists for histogram:") 
    merged_original=[[i]*j for (i,j) in distribution_original.items()]
    merged_permuted=[[i]*j for (i,j) in distribution_permuted.items()]
    list_original=list(itertools.chain.from_iterable(merged_original))
    list_permuted=list(itertools.chain.from_iterable(merged_permuted))
    
    plt.hist(list_original,bins=20,histtype='stepfilled',normed=False,color='b',label='hg19 original')
    plt.hist(list_permuted,bins=20,histtype='stepfilled',normed=False,color='r',alpha=0.5,label='local genome permutations')
    plt.title(motif_name+" at p-thresh="+str(args.p_val))
    plt.xlabel("Motif Score")
    plt.ylabel("Number of hits in ENCODE DNAse Union Set")
    plt.legend()
    plt.savefig(motif_name.split('/')[-1]+"."+str(args.p_val)+".png")
    
    
    
if __name__=="__main__":
    main() 