import argparse
import h5py
import numpy as np
import pdb
def parse_args():
    parser=argparse.ArgumentParser()
    parser.add_argument("--train_hdf5")
    parser.add_argument("--test_hdf5")
    parser.add_argument("--valid_hdf5")
    parser.add_argument("--out_normalized_train_hdf5")
    parser.add_argument("--out_normalized_valid_hdf5")
    parser.add_argument("--out_normalized_test_hdf5")
    parser.add_argument("--out_means")
    parser.add_argument("--out_std")
    return parser.parse_args()

def main():
    args=parse_args()
    train_data=h5py.File(args.train_hdf5,'r')
    valid_data=h5py.File(args.valid_hdf5,'r')
    test_data=h5py.File(args.test_hdf5,'r')
    print("opened hdf5 files for reading")

    #get mean & stddev

    num_cols=train_data['X']['sequence'].shape[1]
    train_x=train_data['X']['sequence'] 
    '''
    means=np.zeros((num_cols,))
    std_devs=np.zeros((num_cols,))
    for c in range(num_cols):
        means[c]=np.mean(train_x[:,c])
        std_devs[c]=np.std(train_x[:,c])
        print(str(c))
    print("computed means & std devs")
    #avoid division by 0 errors! 
    std_devs[std_devs==0]=1 
    np.save(args.out_means,means)
    np.save(args.out_std,std_devs)
    '''
    means=np.load(args.out_means)
    std_devs=np.load(args.out_std)
    print("means:"+str(means.shape))
    print("st_devs:"+str(std_devs.shape))
    #generate output files!
    outf_train=h5py.File(args.out_normalized_train_hdf5,'w')
    outf_valid=h5py.File(args.out_normalized_valid_hdf5,'w')
    outf_test=h5py.File(args.out_normalized_test_hdf5,'w')
    print("opened all the hdf5's")
    outf_train.create_group("Y")
    train_data.copy("Y/output/",outf_train["/Y"])
    print("copied Y train")
    train_x=train_data['X']['sequence']
    nrow_train=train_x.shape[0]
    normalized_train_x=outf_train.create_dataset("X/sequence",shape=(nrow_train,1),maxshape=(nrow_train,None))
    normalized_train_x[:]=np.expand_dims((train_x[:,0]-means[0])/std_devs[0],axis=1)
    #iterate through each column in df & write the normalized output
    col_count=1
    for c in range(1,num_cols):
        if c%1000==0:
            print(str(c))
        normalized_train_x.resize(col_count+1,axis=1)
        new_chunk=(train_x[:,c]-means[c])/std_devs[c]
        normalized_train_x[:,-1]=new_chunk
        col_count+=1
        
    #normalized_train_x=outf_train.create_dataset("X/sequence",data=(train_x-means)/std_devs,chunks=True)
    outf_train.flush()
    outf_train.close()
    print("copied training data")

    outf_valid.create_group("Y")
    valid_data.copy("Y/output/",outf_valid["/Y"])
    print("copied Y valid")
    valid_x=valid_data['X']['sequence']
    nrow_valid=valid_x.shape[0]
    normalized_valid_x=outf_valid.create_dataset("X/sequence",shape=(nrow_valid,1),maxshape=(nrow_valid,None))
    normalized_valid_x[:]=np.expand_dims((valid_x[:,0]-means[0])/std_devs[0],axis=1) 
    col_count=1
    for c in range(1,num_cols):
        if c%1000==0:
            print(str(c))
        normalized_valid_x.resize(col_count+1,axis=1)
        new_chunk=(valid_x[:,c]-means[c])/std_devs[c]
        normalized_valid_x[:,-1]=new_chunk
        col_count+=1
    outf_valid.flush()
    outf_valid.close()
    print("copied valid data")



    outf_test.create_group("Y")
    test_data.copy("Y/output/",outf_test["/Y"])
    print("copied Y test")
    test_x=test_data['X']['sequence']
    nrow_test=test_x.shape[0]
    normalized_test_x=outf_test.create_dataset("X/sequence",shape=(nrow_test,1),maxshape=(nrow_test,None))
    normalized_test_x[:]=np.expand_dims((test_x[:,0]-means[0])/std_devs[0],axis=1)
    col_count=1
    for c in range(1,num_cols):
        if c%1000==0:
            print(str(c))
        normalized_test_x.resize(col_count+1,axis=1)
        new_chunk=(test_x[:,c]-means[c])/std_devs[c]
        normalized_test_x[:,-1]=new_chunk
        col_count+=1
    outf_test.flush()
    outf_test.close()
    print("copied test data")


if __name__=="__main__":
    main()
    
    
