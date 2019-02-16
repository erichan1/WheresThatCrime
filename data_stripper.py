import csv
import re
import time
import datetime

def to_dt(inputTime): 
    ret = int(inputTime[0:1])*3600 + int(inputTime[3:4])*60
    return str(ret)

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

if __name__ == '__main__':
    fp = input("What is the input path? ")
    op = input("What is the output path? ")
    with open(fp, newline='') as csvfile:
        with open(op, 'a') as output_file:
            reader = csv.DictReader(csvfile)    
            for row in reader:
                if (row['Date'].endswith("2017")):
                    output_file.write(to_dt(row['Time']) + "," + coordinates(row['Location']) + ',' + to_severity(row['Category']) + "\n")