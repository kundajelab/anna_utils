#randomly sample a given number of regions from a bed file
import argparse
import pandas as pd 
def parse_args():
    parser=argparse.ArgumentParser(description="randomly sample a given number of regions from a bed file")
    parser.add_argument("--bed")
    parser.add_argument("--n",type=int)
    parser.add_argument("--outf")
    return parser.parse_args()

def main():
    args=parse_args()
    bed=pd.read_csv(args.bed,sep='\t',header=None)
    sampled=bed.sample(args.n)
    sampled.to_csv(args.outf,sep='\t',index=False,header=False)

if __name__=="__main__":
    main()
    
