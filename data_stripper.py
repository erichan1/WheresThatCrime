import csv
import re
import time
import datetime
import numpy as np

#def to_dt(inputTime): 
#    ret = int(inputTime[0:1])*3600 + int(inputTime[3:4])*60
#    return str(ret)

def to_timestamp(day, inputTime):
    output = int(time.mktime(datetime.datetime.strptime(day, "%m/%d/%Y").timetuple())) +int(inputTime[0:1])*3600 + int(inputTime[3:4])*60
    output = int(output/3600)
    print("New timestamp : " + str(output))
    #output = datetime.datetime.fromtimestamp(output).isoformat()
    return str(output)

def coordinates(inputCoord): 
    arbitrary = inputCoord[1:-1]
    return arbitrary

def to_severity(severity):
    #NON-CRIMINAL ROBBERY,  ASSAULT, VANDALISM, SECONDARY CODES, BURGLARY, LARCENY/THEFT, DRUG/NARCOTIC
    #WARRANTS VEHICLE THEFT ROBBERY
    if (severity == "ASSAULT"):
        return str(5)
    elif (severity == "ROBBERY"):
        return str(4)
    elif (severity == "VANDALISM" or severity == "BURGARLY" or severity == "VEHICLE THEFT" or severity == "ROBBERY"):
        return str(3)
    elif (severity == "SECONDARY CODES" or severity == "LARCENY/THEFT" or severity == "DRUG/NARCOTIC"):
        return str(2)
    elif (severity == "WARRANTS"):
        return str(2)
    else:
        return str(1)

def retrieve_inputs ():
    my_data = np.genfromtxt('reduced_pattern.csv', delimiter=',', skip_header=0, usecols = (0, 1, 2), replace_space='')
    print(my_data)
    return my_data

def retrieve_outputs (): 
    my_data = np.genfromtxt('reduced_pattern.csv', delimiter=',', skip_head=0, usecols = (3), replace_space='')
    return my_data
        

if __name__ == '__main__':
    fp = input("What is the input path? ")
    op = input("What is the output path? ")
    with open(fp, newline='') as csvfile:
        with open(op, 'a') as output_file:
            reader = csv.DictReader(csvfile)    
            for row in reader:
                if (row['Date'] and row['Date'].endswith("2017")):
                    output_file.write(to_timestamp(row['Date'],row['Time']) + "," + coordinates(row['Location']) + ',' + to_severity(row['Category']) + "\n")
