#save a motif hit matrix to a sparse format
import argparse
import numpy as np 
def parse_args():
    parser=argparse.ArgumentParser(description="save a motif hit matrix to sparse format")
    parser.add_argument('--i')
    parser.add_argument('--outf')
    return parser.parse_args() 
    
def main():
    args=parse_args()
    data=np.load(args.i)
    nonzero=np.nonzero(data)
    c1=np.expand_dims(nonzero[0],axis=1)+1 #change 0-indexing to 1-indexing for use with MEDUSA
    c2=np.expand_dims(nonzero[1],axis=1)+1 
    c3=np.ones_like(c1)
    combined=np.concatenate((c1,c2,c3),axis=1)
    np.savetxt(args.outf,combined,fmt='%i',delimiter='\t')

if __name__=="__main__":
    main()
    
