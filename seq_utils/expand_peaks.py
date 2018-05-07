#threshold a narrowPeak file to a region of a specified size around the summit.
import argparse
import math

def parse_args():
    parser=argparse.ArgumentParser(description="expand peak to desired length")
    parser.add_argument("--bed_file")
    parser.add_argument("--target_length",type=int,default=1000) 
    parser.add_argument("--outf")
    return parser.parse_args()

def main():
    args=parse_args()
    outf=open(args.outf,'w')
    bed_file=open(args.bed_file,'r').read().strip().split('\n')
    for line in bed_file:
        tokens=line.split('\t')
        chrom=tokens[0]
        start_pos=int(tokens[1])
        end_pos=int(tokens[2])
        padding=args.target_length - (end_pos - start_pos)
        left_pad=math.floor(padding/2)
        right_pad=math.ceil(padding/2)
        new_start=start_pos-left_pad
        new_end=end_pos+right_pad 
        outf.write(chrom+'\t'+str(new_start)+'\t'+str(new_end)+'\n')
        
        

if __name__=="__main__":
    main()
    
    

