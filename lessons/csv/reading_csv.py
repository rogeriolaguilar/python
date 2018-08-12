import csv
import os

FILENAME=os.getcwd()+'/lessons/csv/hightemp.csv'

def read_csv(csv_name, keyname):
    print(csv_name)
    table = {}
    with open(csv_name) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            table[row[keyname]] = row
    
    return table


result = read_csv(FILENAME, 'City')
print("Baghdad in Jan =", result['Baghdad']['Jan'])