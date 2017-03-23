import numpy as np 
np.random.seed(1234) 
from keras.layers import Input
from keras.objectives import binary_crossentropy
from keras.metrics import * 
from keras.models import Model 
from keras.layers.core import Dropout, Reshape, Dense, Activation, Flatten
from keras.layers.convolutional import Convolution2D, MaxPooling2D
from keras.optimizers import Adam
from keras.constraints import maxnorm;
from keras.layers.advanced_activations import PReLU
from keras.layers.normalization import BatchNormalization
from keras.regularizers import l1, l2, activity_l1, activity_l2
                                


input_config=Input(shape=(4,1,2000),name="sequence")
conv1=Convolution2D(nb_filter=300,nb_row=4,nb_col=30,
                    init="glorot_uniform",
                    activity_regularizer=activity_l1(1e-5),
                    W_constraint=maxnorm(m=7,axis=1))(input_config)
relu1=ReLU(name="relu1")(conv1)
avpool1=AveragePooling2D(pool_size=(1,4))(relu1)
conv2=Convolution2D(nb_filter=200,nb_row=1,nb_col=11,
                    init="glorot_uniform",
                    activity_regularizer=activity_l1(1e-5),
                    W_constraint=maxnorm(m=7,axis=1))(avpool1)
batchnorm1=BatchNormalization(mode=0, axis=1)(conv2)
relu2=ReLU(name="relu2")(batchnorm1)
avpool2=AveragePooling2D(pool_size=(1,3))(relu2)
conv3=Convolution2D(nb_filter=200,nb_row=1,nb_col=7,
                    init="glorot_uniform",
                    activity_regularizer=activity_l1(1e-5),
                    W_constraint=maxnorm(m=7,axis=1))(avpool2)
batchnorm2=BatchNormalization(mode=0, axis=1)(conv3)
relu3=ReLU(name="relu3")(batchnorm2)
avpool3=AveragePooling2D(pool_size=(1,3))(relu3)
flatten=Flatten()(avpool3)
dense1=Dense(1000,activity_regularizer=activity_l1(1e-5),
             W_constraint=maxnorm(m=7))(flatten)
prelu1=PReLU()(dense1)
dropout1=Dropout(0.3)(prelu1)
dense2=Dense(1000,activity_regularizer=activity_l1(1e-5),
             W_constraint=maxnorm(m=7))(dropout1)
prelu2=PReLU()(dense2)
dropout2=Dropout(0.3)(prelu2)
output_config=Dense(12,
                    init="glorot_uniform",
                    name="output",
                    activation="sigmoid",
                    W_regularizer=l2(1e-3),
                    W_constraint=maxnorm(m=7,axis=1))(dropout2)
model=Model(input=input_config,output=output_config)
adam=Adam(lr=0.001, beta_1=0.9, beta_2=0.999, epsilon=1e-08, decay=0.0)

#w0=[float(i) for i in open(w0_file,'r').read().strip().split('\n')]
#w1=[float(i) for i in open(w1_file,'r').read().strip().split('\n')]
#loss=get_weighted_binary_crossentropy(w0_weights=w0,w1_weights=w1)
model.compile(optimizer=adam,loss='binary_crossentropy',metrics=["positive_accuracy","negative_accuracy","precision","recall"])

