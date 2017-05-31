import numpy as np
data=np.load("mat.npy")
nonzero=0
for line in data:
    maxval=np.max(line)
    if maxval > 0:
        nonzero+=1
print(str(nonzero))
