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
        data_batch=dict()
        data_batch.update(x_batch)
        data_batch.update(y_batch)
        yield data_batch



def create_model(w0_file,w1_file):
    np.random.seed(1234)
    from keras.layers.core import Dense, Dropout, Activation
    from keras.layers import Input
    from keras.legacy.models import Graph
    from keras.layers.advanced_activations import PReLU
    from keras.optimizers import Adam
    from keras.regularizers import ActivityRegularizer,l2
    from keras.objectives import get_weighted_binary_crossentropy
    from keras.constraints import maxnorm
    from keras.metrics import * 

    model=Graph()
    model.add_input(name="sequence",input_shape=(15360,))
    model.add_node(Dense(1000,
                         init="glorot_uniform",
                         W_regularizer=l2(1e-6),
                         W_constraint=maxnorm(m=7,axis=1))
                   ,name="dense1",
                   input="sequence")
    model.add_node(PReLU(),
                   name="prelu1",
                   input="dense1")
    model.add_node(Dropout(p=0.5),
                   name="dropout1",
                   input="prelu1")
    model.add_node(Dense(500,
                         init="glorot_uniform",
                         W_regularizer=l2(1e-6),
                         W_constraint=maxnorm(m=7,axis=1)),
                   name="dense2",
                   input="dropout1")
    model.add_node(PReLU(),
                   name="prelu2",
                   input="dense2")
    model.add_node(Dropout(p=0.5),
                   name="dropout2",
                   input="prelu2")
    model.add_node(Dense(12,
                         init="glorot_uniform",
                         W_regularizer=l2(1e-3),
                         W_constraint=maxnorm(m=7,axis=1)),
                   name="dense_final",
                   input="prelu2")
    model.add_node(Activation("sigmoid"),
                   name="activation_final",
                   input="dense_final")
    model.add_output(name="output",input="activation_final")
    adam=Adam(lr=0.001, beta_1=0.9, beta_2=0.999, epsilon=1e-08, decay=0.0)
    w0=[float(i) for i in open(w0_file,'r').read().strip().split('\n')]
    w1=[float(i) for i in open(w1_file,'r').read().strip().split('\n')]
    loss={'output':get_weighted_binary_crossentropy(w0_weights=w0,w1_weights=w1)}
    model.compile(optimizer=adam,loss=loss,metrics=["positive_accuracy","negative_accuracy","precision","recall"])
    return model
