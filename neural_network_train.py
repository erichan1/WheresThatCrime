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
import data_stripper

# for each column, subtract by min val, then divide by max val. 
def normalize_data(x_data):
    new_x = x_data.copy()
    shape = new_x.shape
    for i in range(shape[1]):
        minVal = np.min(new_x[:,i])
        new_x[:,i] -= minVal
        maxVal = np.max(new_x[:,i])
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
    model.add(Dropout(0.5))

    # second layer in the model. is dense. similar parameters.  
    model.add(Dense(20, kernel_initializer='normal'))
    model.add(BatchNormalization())
    model.add(Activation('relu'))
    model.add(Dropout(0.5))
    
    # output layer. Has a single neuron, which will hold estimated severity value. 
    model.add(Dense(1, kernel_initializer='normal'))
    model.add(Activation('linear'))
    
    model.compile(optimizer='rmsprop',
                  loss='mean_absolute_error',
                  metrics=['mean_absolute_error'])

    return model 

# create and train NN ensemble
def create_train_NN_ensemble(X_train, Y_train, n_estimators):
    input_size = X_train.shape[1]
    modelList = []
    for i in range(n_estimators):
        this_model = create_NN(input_size)
        this_model.fit(X_train, Y_train, epochs=10)
        modelList.append(this_model)
    return modelList

if __name__ == '__main__':
    # The pipeline should look like: 
    # Location, timestamp from user = X_test -> model.predict(X_test) -> predicted severity on map

    # do data import stuff here. Below is commented code
    # lat1: 37.77756, lo1: -122.463547
    # lat2: 37.782783, lo2: -122.470499
    X_train = data_stripper.retrieve_inputs()
    Y_train = data_stripper.retrieve_outputs()

    X_train_N = normalize_data(X_train)

    # model class created. Not fitted on data yetX_train_n. This model will perform terribly. 
    modelList = create_train_NN_ensemble(X_train_N, Y_train, 10)

    for i, model in enumerate(modelList): 
        model.save('models/NN_ensemble/danger_model{}.h5'.format(i))

