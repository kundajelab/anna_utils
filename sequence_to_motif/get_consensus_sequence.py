#generates consensus sequence from frequency motif matrix
import argparse
import numpy as np
import pdb

def parse_args():
    parser=argparse.ArgumentParser(description="generate consensus sequence from frequency motif matrix")
    parser.add_argument("--pwm_source_file")
    parser.add_argument("--outf")
    return parser.parse_args()

def translate(consensus):
    outstring=""
    for entry in consensus:
        if entry==0:
            outstring=outstring+"A"
        elif entry==1:
            outstring=outstring+"C"
        elif entry==2:
            outstring=outstring+"G"
        elif entry==3:
            outstring=outstring+"T"
        else:
            raise(Exception("Invalid maximum index specified:"+str(entry))) 
    return outstring
def main():
    args=parse_args()
    outf=open(args.outf,'w') 
    pwm_sources=open(args.pwm_source_file,'r').read().strip().split('\n')
    for source in pwm_sources:
        data=np.loadtxt(source)
        consensus=np.argmax(data,axis=0)
        #get the corresponding bases
        outstring=translate(consensus) 
        outf.write(source+'\t'+outstring+'\n') 
    

if __name__=="__main__":
    main()
    
