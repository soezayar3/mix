import csv

nrc_list = []
with open('nrc.csv', 'r') as f:
    data = csv.reader(f)
    for row in data:
        nrc_list = str(row)
        #print(nrc_list)