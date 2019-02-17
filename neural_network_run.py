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
        print(maxVal)
        if(maxVal != 0):
            new_x[:,i] /= maxVal
    return new_x

def write_file(filename, X, pred_Y):
    '''
    Insert some text
    '''
    X_shape = X.shape
    Y_shape = len(pred_Y)

    results = np.zeros((Y_shape, X_shape[1] + 1))
    results[:, 0:X.shape[1]] = X
    results[:, -1] = pred_Y
        
    with open(filename,'w') as f:
        f.write('dayofweek, latitude, longitude, pred_Severity \n')
        writer=csv.writer(f,delimiter=',')
        writer.writerows(results)
    f.close()
# input is (x, y). 
# generates a square of (x,y) within 0.5 lat degree of the given lat
def generate_X_test(dayofweek, latitude, longitude):
    numAxisPoints = 101 # the number of points on X and Y. total # points is this squared. 
    T = np.array([dayofweek] * numAxisPoints**2)
    X = np.linspace(longitude - 0.044, longitude + 0.034, numAxisPoints)
    Y = np.linspace(latitude - 0.044, latitude + 0.034, numAxisPoints)
    X_test = np.zeros((numAxisPoints**2, 3))
    X_test[:,0] = dayofweek

    XY = np.array(np.meshgrid(X, Y)).T.reshape(-1, 2)

    X_test[:,1:3] = XY
    return X_test

# makes the trends in the data more clear -_o
def adjustData(pred_Y):
    min_val = np.min(pred_Y)
    max_val = np.max(pred_Y)
    diff = max_val - min_val
    pred_Y = (pred_Y - min_val) / diff * 2 + 2
    return pred_Y 

# add a bit of noise to the data
def addNoise(pred_Y, maxOffset):
    for val in pred_Y:
        val += np.random.uniform(-1 * maxOffset, maxOffset) 
    return pred_Y



if __name__ == '__main__':
    # test_dayofweek = input("What day of the week? \n")
    # test_longitude = input("What latitude (y)? \n")
    # test_latitude = input("What longitude (x)? \n")

    test_dayofweek = 4
    test_longitude = 37.755
    test_latitude = -122.450 



    X_test = generate_X_test(int(test_dayofweek), float(test_latitude), float(test_longitude))
    X_test_N = normalize_data(X_test)
    
    model = keras.models.load_model('models/danger_modelv1.h5')

    predicted_severity = model.predict(X_test_N)
    predicted_severity = predicted_severity.reshape(-1)
    predicted_severity = adjustData(predicted_severity)
    predicted_severity = addNoise(predicted_severity, 5)

    write_file('models/danger_predictionsv2.csv', X_test, predicted_severity)

    