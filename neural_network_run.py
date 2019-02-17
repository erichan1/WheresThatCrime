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

def write_file(filename, X, pred_Y):
    '''
    Insert some text
    '''
    new_X, new_pred_Y = zip(*sorted(zip(X,pred_Y)))
    new_X_array = []
    for value in list(new_X):
        new_X_array.append(int(value))
        
    with open(filename,'w') as f:
        f.write('X,pred_Y\n')
        writer=csv.writer(f,delimiter=',')
        writer.writerows(zip(new_X_array,list((new_pred_Y))))
    f.close()
# input is (x, y). 
# generates a square of (x,y) within 0.5 lat degree of the given lat
def generate_X_test(longitude, latitude):
    X = np.linspace(longitude - 0.5, longitude + 0.5, 21)
    Y = np.linspace(latitude - 0.5, latitude + 0.5, 21)
    return np.array([X, Y])

if __name__ == '__main__':
	test_longitude = input("What longitude (x)?")
	test_latitude = input("What latitude (y)?")
	X_test = generate_X_test(test_longitude, test_latitude)

	model = load_model('danger_modelv1.h5')

	predicted_severity = model.predict(X_test)

	write_file('danger_predictionsv1.csv', X_test, predicted_severity)

	