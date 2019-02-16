import numpy as np
import pandas as pd


if __name__ == '__main__':
    crime_data_csv = 'SF_Crime_Heat_Map_Stripped_Minimal.csv'
    crime_data = pd.read_csv(crime_data_csv, sep=',') 
    #crime_data = np.genfromtxt(crime_data_csv, skip_header=1, delimiter=',', encoding="utf8")
    #Note: np array seems to prefer integer type
    print (crime_data)
    print ("Ok" )