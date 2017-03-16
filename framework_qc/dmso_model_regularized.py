import numpy as np 
def data_generator(hdf5_source,args):
    num_generated=0
    input_modes=hdf5_source['X'].keys()
    output_modes=hdf5_source['Y'].keys()
    total_entries=hdf5_source['X'][input_modes[0]].shape[0]
    start_index=0
    batch_size=args.batch_size 
    while True:
        if(num_generated >=total_entries):
            start_index=0
        x_batch={}
        y_batch={}
        end_index=start_index+batch_size 
        for input_mode in input_modes:
            x_batch[input_mode]=hdf5_source['X'][input_mode][start_index:end_index]
        for output_mode in output_modes:
            y_batch[output_mode]=hdf5_source['Y'][output_mode][start_index:end_index]
        num_generated+=batch_size 
        start_index=end_index
        yield tuple([x_batch,y_batch])


def create_model(w0_file,w1_file):
    np.random.seed(1234) 
    from keras.layers.core import Dense, Dropout
    from keras.layers import Input
    from keras.models import Model
    from keras.layers.advanced_activations import PReLU
    from keras.optimizers import Adam
    from keras.regularizers import ActivityRegularizer,l2
    from keras.objectives import get_weighted_binary_crossentropy
    from keras.constraints import maxnorm
    from keras.metrics import * 

    input_config=Input(shape=(15360,),name="sequence")
    dense1=Dense(1000,
                 name="dense1",
                 init="glorot_uniform",
                 W_regularizer=l2(1e-6),
                 W_constraint=maxnorm(m=7,axis=1))(input_config)
    prelu1=PReLU(name="prelu1")(dense1)
    dropout1=Dropout(p=0.5,name="dropout1")(prelu1)
    dense2=Dense(500,
                 init="glorot_uniform",
                 W_regularizer=l2(1e-6),
                 W_constraint=maxnorm(m=7,axis=1))(dropout1)
    prelu2=PReLU(name="prelu2")(dense2)
    dropout2=Dropout(p=0.5)(prelu2)
    output_config=Dense(12,
                        init="glorot_uniform",
                        name="output",
                        activation="sigmoid",
                        W_regularizer=l2(1e-3),
                        W_constraint=maxnorm(m=7,axis=1))(dropout2)
    model=Model(input=input_config,output=output_config)
    adam=Adam(lr=0.001, beta_1=0.9, beta_2=0.999, epsilon=1e-08, decay=0.0)

    w0=[float(i) for i in open(w0_file,'r').read().strip().split('\n')]
    w1=[float(i) for i in open(w1_file,'r').read().strip().split('\n')]
    loss=get_weighted_binary_crossentropy(w0_weights=w0,w1_weights=w1)
    model.compile(optimizer=adam,loss=loss,metrics=["positive_accuracy","negative_accuracy","precision","recall"])
    return model


