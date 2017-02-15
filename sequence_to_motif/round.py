import sys
import numpy as np
data=np.loadtxt(sys.argv[1])
#round!
data[:,0]=np.round(data[:,0],2)
#clump the dictionary
vals=dict()
outf=open(sys.argv[1]+'.sorted','w')
for i in range(data.shape[0]):
    key=data[i,0]
    val=data[i,1]
    if key not in vals:
        vals[key]=val
    else:
        vals[key]+=val
keys=vals.keys()
keys.sort() 
for key in keys:
    outf.write(str(key)+'\t'+str(vals[key])+'\n')
    
