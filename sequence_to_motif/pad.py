#pad the specified bed file to the desired length
import argparse
import math 
def parse_args():
    parser=argparse.ArgumentParser(description='pads each peak in the provided bed file to the specified length')
    parser.add_argument('--input_bed')
    parser.add_argument('--desired_length',type=int)
    parser.add_argument('--output_bed')
    return parser.parse_args() 
def main():
    args=parse_args()
    outf=open(args.output_bed,'w')
    data=open(args.input_bed,'r').read().strip().split('\n')
    for line in data:
        tokens=line.split('\t')
        chrom=tokens[0]
        startpos=int(tokens[1])
        endpos=int(tokens[2])
        peak_width=endpos-startpos
        topad=args.desired_length-peak_width
        startpos-=int(math.floor(topad/2))
        endpos+=int(math.ceil(topad/2))
        outf.write(chrom+'\t'+str(startpos)+'\t'+str(endpos)+'\n')
        
if __name__=="__main__":
    main() 
