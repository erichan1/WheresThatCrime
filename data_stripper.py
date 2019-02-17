import csv
import re
import time
import datetime
import numpy as np

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

def reint_day(day):
       if (day == "Sunday"):
           return str(1)
       elif (day == "Monday"):
           return str(2)
       elif (day == "Tuesday"):
           return str(3)
       elif (day == "Wednesday"):
           return str(4)
       elif (day == "Thursday"):
           return str(5)
       elif (day == "Friday"):
           return str(6)
       elif (day == "Saturday"):
           return str(7)
       else:
           return "WARNING! INVALID ARG PASSED TO REINT_DAY"

def retrieve_inputs ():
    my_data = np.genfromtxt('current_stat.csv', delimiter=',', skip_header=0, usecols = (0, 1, 2), replace_space='')
    #print(my_data)
    return my_data

def retrieve_outputs (): 
    my_data = np.genfromtxt('current_stat.csv', delimiter=',', skip_head=0, usecols = (3), replace_space='')
    return my_data

def retrieve_test(): 
    my_data = np.genfromtxt('current_model.csv', delimiter=',', skip_head=0, replace_space='')
    return my_data

def get_data(mo, yr, rl): #rl would be really copying, if false it'll instead install 
    inp = "../SF_Crime_Heat_Map.csv"
    if (rl == True):
        otp = "models/current_stat.csv"   
    else: 
        otp = "models/current_model.csv"
    with open(inp, newline='') as csvfile:
        with open(otp, 'a') as output_file:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if (row['Date'] and row['Date'].endswith(yr) and row['Date'].startswith(mo)):
                    if (rl):
                        output_file.write(reint_day(row['DayOfWeek']) + "," + coordinates(row['Location']) + ',' + to_severity(row['Category']) + "\n")
                    else: 
                        output_file.write(reint_day(row['DayOfWeek']) + ',' + coordinates(row['Location']) +'\n')

if __name__ == '__main__':
    print("Generating files, please wait ...")
    get_data("01","2017", True)
    print("Generated current stats at current_stat.csv")
    get_data("02","2017", False)
    print("Generated future components at current_mode.csv")