import csv

class Result():
    # Compares results from QUINA lottery. 5 numbers game.
    def __init__(self, result, dataset):
     self.result =  result
     self.dataset =  dataset

    def calculate(self):    
      with open(self.result, newline='') as x:
        rslt = csv.reader(x)
        for line in rslt:
            result = line


        with open(self.dataset, newline='') as f:
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
             
             


def main():
    a = Result('result.csv', 'dataset.csv')
    a.calculate()

main()
