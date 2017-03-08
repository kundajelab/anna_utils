import argparse
import h5py
import numpy as np
def parse_args():
    parser=argparse.ArgumentParser()
    parser.add_argument("--train_hdf5")
    parser.add_argument("--test_hdf5")
    parser.add_argument("--valid_hdf5")
    parser.add_argument("--out_normalized_train_hdf5")
    parser.add_argument("--out_normalized_valid_hdf5")
    parser.add_argument("--out_normalized_test_hdf5")
    return parser.parse_args()

def main():
    args=parse_args()
    train_data=h5py.File(args.train_hdf5,'r')
    valid_data=h5py.File(args.valid_hdf5,'r')
    test_data=h5py.File(args.test_hdf5,'r')
    print("opened hdf5 files for reading")

    #get mean & stddev
    '''
    num_cols=train_data['X']['sequence'].shape[1]
    means=np.zeros((num_cols,))
    std_devs=np.zeros((num_cols,))
    train_x=train_data['X']['sequence'] 
    for c in range(num_cols):
        means[c]=np.mean(train_x[:,c])
        std_devs[c]=np.std(train_x[:,c])
        print(str(c))
    print("computed means & std devs")
    #avoid division by 0 errors! 
    std_devs[std_devs==0]=1 
    np.save("means.npy",means)
    np.save("std_devs.npy",std_devs)
    '''
    means=np.load("means.npy")
    std_devs=np.load("std_devs.npy")
    #generate output files!
    outf_train=h5py.File(args.out_normalized_train_hdf5,'w')
    outf_valid=h5py.File(args.out_normalized_valid_hdf5,'w')
    outf_test=h5py.File(args.out_normalized_test_hdf5,'w')
    print("opened all the hdf5's")
    
    outf_train.create_group("Y")
    train_data.copy("Y/output/",outf_train["/Y"])
    print("copied Y train")
    train_x=train_data['X']['sequence'] 
    normalized_train_x=outf_train.create_dataset("X/sequence",data=(train_x-means)/std_devs,chunks=True)
    outf_train.flush()
    outf_train.close()
    print("copied training data")
    
    outf_valid.create_group("Y")
    valid_data.copy("Y/output/",outf_valid["/Y"])
    print("copied Y valid")
    valid_x=valid_data['X']['sequence'] 
    normalized_valid_x=outf_valid.create_dataset("X/sequence",data=(valid_x-means)/std_devs,chunks=True)
    outf_valid.flush()
    outf_valid.close()
    print("copied valid data")

    outf_test.create_group("Y")
    test_data.copy("Y/output/",outf_test["/Y"])
    print("copied Y test")
    test_x=test_data['X']['sequence'] 
    normalized_test_x=outf_test.create_dataset("X/sequence",data=(test_x-means)/std_devs,chunks=True)
    outf_test.flush()
    outf_test.close()
    print("copied test data")
    
if __name__=="__main__":
    main()
    
    
