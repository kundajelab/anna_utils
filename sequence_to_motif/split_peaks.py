import sys
data=open(sys.argv[1],'r').read().strip().split('\n')
outf=open(sys.argv[2],'w')
for line in data:
    tokens=line.split('_') 
    endpos=tokens[-1]
    startpos=tokens[-2]
    chrom=tokens[0:-2]
    outf.write('_'.join(chrom)+'\t'+startpos+'\t'+endpos+'\n')
    
