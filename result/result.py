"""import csv

with open('file.csv') as file:
    reader = csv.DictReader(file)

for row in reader:
    print(row)"""

import csv
with open('result.csv', newline='') as x:
    rslt = csv.reader(x)
    for line in rslt:
        result = line


with open('dataset.csv', newline='') as f:
    dataset = csv.reader(f)
    l = 0
    for row in dataset:
         l =l + 1
         for i in row:
             if result[0] == i:
                 print ("Match in " + str(row) + " value " + str(i) + " in line " + str(l))
             elif result[1] == i:
                 print ("Match in " + str(row) + " value " + str(i) + " in line " + str(l))
             elif result[2] == i:
                 print ("Match in " + str(row) + " value " + str(i) + " in line " + str(l))
             elif result[3] == i:
                 print ("Match in " + str(row) + " value " + str(i) + " in line " + str(l))
             elif result[4] == i:
                 print ("Match in " + str(row) + " value " + str(i) + " in line " + str(l))
             
             
             