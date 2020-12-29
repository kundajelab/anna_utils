import sys
import pandas as pd
fname=sys.argv[1]
basename=fname.split('/')[-1] 
data=pd.read_csv(fname,header=None,sep='\t',error_bad_lines=False) 
chroms=['chr'+str(i) for i in range(1,23)]+['chrX','chrY']
print(chroms)
for chrom in chroms:
    subset=data[data[0]==chrom]
    subset.to_csv(chrom+'.'+basename,header=False,index=False,sep='\t')
    print("wrote:"+str(chrom)+"."+str(basename))
    
