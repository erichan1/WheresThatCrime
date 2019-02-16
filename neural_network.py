import matplotlib.pyplot as plt
import numpy as np
import keras
from keras.models import Sequential
from keras.layers import Dense, Activation, Dropout
from keras.layers import Conv2D, MaxPooling2D, Flatten, BatchNormalization
from keras import regularizers
from sklearn.model_selection import KFold
from keras.utils import to_categorical
from sklearn.metrics import roc_auc_score
import csv

# for each column, divide all of it by its max value
def normalize_data(x_data):
    new_x = x_data.copy()
    shape = new_x.shape
    for i in range(shape[1]):
        col = new_x[:,i]
        maxVal = np.max(col)
        new_x[:,i] /= maxVal
    return new_x


def cross_val_NN(model, x_data, y_data):
    kf = KFold(n_splits=5)
    training_accuracy = []
    test_accuracy = []
    weights = model.get_weights()
    for train_index, test_index in kf.split(x_data):
        model.set_weights(weights)
        x_train_fold, x_test_fold = x_data[train_index], x_data[test_index]
        y_train_fold, y_test_fold = y_data[train_index], y_data[test_index]
        training_model = model.fit(x_train_fold, y_train_fold, epochs=30, batch_size=1000)
        training_accuracy.append(model.evaluate(x=x_train_fold, y=y_train_fold)[1])
        test_accuracy.append(model.evaluate(x=x_test_fold,y=y_test_fold)[1])
        

    training_accuracy = np.array(training_accuracy)
    test_accuracy = np.array(test_accuracy)

    return (training_accuracy, test_accuracy)


def create_NN(input_size):
    # encapsulate the model I've built so far
    # if you want to play w model parameters do it here
    # may add parameters to this function so I can do sensitivity training

    # means this is a dense neural network model class. 
    model = Sequential()

    # dense input layer. input size is defined. weights are initialized to normal dist. 
    model.add(Dense(input_size, input_shape=(input_size,), kernel_initializer='normal'))
    # normalize 
    model.add(BatchNormalization())
    # For each neuron, it receives value (w1x1 + w2x2 + ...), where w is weight and x is neuron input
    # relu is a function which you apply to input into neuron to get output. 
    # relu (w1x1 + w2x2 + ...) -> neuron output
    model.add(Activation('relu'))
    # randomly sets weights to zero. prevents overfitting.  
    model.add(Dropout(0.4))
    
    # second layer in the model. is dense. similar parameters.  
    model.add(Dense(20, kernel_initializer='normal'))
    model.add(BatchNormalization())
    model.add(Activation('relu'))
    model.add(Dropout(0.4))
    
    # output layer. Has a single neuron, which will hold estimated severity value. 
    model.add(Dense(1, kernel_initializer='normal'))
    model.add(Activation('linear'))
    
    model.compile(optimizer='adam',
                  loss='mean_absolute_error',
                  metrics=['mean_absolute_error'])

    return model 

if __name__ == '__main__':
    # Note: This code doesn't work yet. Like at all. The functions work on their own though. 
    # v unsure how to integrate this python with webdev. 
    # The pipeline should look like: 
    # Location, timestamp from user = X_test -> model.predict(X_test) -> predicted severity on map

    # do data import stuff here. Below is commented code

    ## X_train = ???
    ## Y_train = ???
    ## X_test = ???

    # model class created. Not fitted on data yet. This model will perform terribly. 
    model = create_NN(X_train.shape[1])

    model.fit(X_train, Y_train)

    # given a 
    predicted_severity = model.predict(X_test)



