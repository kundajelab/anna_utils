import argparse
import pysam
import random

def parse_args():
    parser=argparse.ArgumentParser(description='permute the genome in specified local bins')
    parser.add_argument('--reference',help='reference fasta file')
    parser.add_argument('--out_prefix',help='output file prefix')
    parser.add_argument('--chrom_sizes',help='file containing sizes of chromosomes')
    parser.add_argument('--bin_size',type=int,help='bin sizes for scanning reference genome',default=1000)
    parser.add_argument('--chrom',nargs="+",help='chromosome',default=None)
    return parser.parse_args()

def parse_chrom_sizes(chrom_sizes_file):
    chrom_sizes=dict()
    with open(chrom_sizes_file) as f:
        data=f.read().strip().split('\n')
        for line in data:
            tokens=line.split('\t')
            chrom_sizes[tokens[0]]=int(tokens[1])
    return chrom_sizes 

def main():
    args=parse_args()
    reference=pysam.FastaFile(args.reference)
    chrom_sizes=parse_chrom_sizes(args.chrom_sizes)
    if args.chrom==None:
        chroms=chrom_sizes.keys() 
    else:
        chroms=args.chrom
    for chrom in chroms:
        outf=open(args.out_prefix+"_"+chrom+".permuted.fasta",'w')
        outf.write(">"+chrom+"\n")
        pos_start=0
        pos_end=pos_start+args.bin_size
        while pos_start < chrom_sizes[chrom]:
            if pos_start %1000000==0:
                print("pos_start:"+str(pos_start)+"/"+str(chrom_sizes[chrom]))
            seq=reference.fetch(chrom,pos_start,pos_end)
            #permute!!
            shuffled=''.join(random.sample(seq,len(seq)))
            #write to output file
            outf.write(shuffled+'\n')
            pos_start=pos_end
            pos_end=pos_start+args.bin_size
        
if __name__=="__main__":
    main() 
