#orders the labels matrices to match the input data matrices.
import sys
import h5py
import os
import numpy as np

labels_filename=sys.argv[1]
out_f=sys.argv[2]
in_prefix=sys.argv[3]
numrows_in_labelfile=int(sys.argv[4])
print(str(sys.argv))

#read in the labels
labels=np.loadtxt(labels_filename,skiprows=1,usecols=range(1,numrows_in_labelfile),dtype=int)
label_pos=np.loadtxt(labels_filename,skiprows=1,usecols=range(0,1),dtype=object)


numtasks=labels.shape[1]
positions=dict()
for i in range(label_pos.shape[0]):
    positions[label_pos[i]]=labels[i]
print("read in labels") 


#create the validation hdf5
f=h5py.File(out_f,'w') 
#load the validation & position numpy array
mat=np.load(in_prefix+'/mat.npy')
#mat=np.expand_dims(mat,axis=1)
#mat=np.expand_dims(mat,axis=2)
print(str(mat.shape))
print("loaded mat.npy") 
arr=f.create_dataset("X/sequence",data=mat,chunks=True)
print("created sequence dataset") 
pos_mat=np.load(in_prefix+'/pos.npy')
print("loaded positions") 
f_labels=np.zeros((pos_mat.shape[0],numtasks))
for i in range(pos_mat.shape[0]):
    entry=pos_mat[i]
    f_labels[i]=positions[entry[0]+"_"+entry[1]+"_"+entry[2]]
print("created positions numpy array") 
out_arr=f.create_dataset("Y/output",data=f_labels,chunks=True)
print("created output dataset") 
f.flush()
f.close()
print("done!")
