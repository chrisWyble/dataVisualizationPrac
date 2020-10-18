from matplotlib import pyplot as plt
import csv

myDict = {}


with open('alabamaCovid19Data_10_13_2020.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    col_count = 0
    for row in csv_reader:
        if line_count == 0:
            for k in row:
                myDict[str(k)] = []
            line_count += 1
        for key in myDict.keys():
            myDict[key].append(row[col_count])
            col_count += 1
        col_count = 0
    
    for k in myDict:
        myDict[k] = myDict[k][1:]
    print(myDict)
    
    
#plt.plot()
#plt.show()