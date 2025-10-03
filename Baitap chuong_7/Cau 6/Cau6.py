import csv
with open('datacsv.csv', newline='', encoding="uft-8") as f:
    reader = csv.reader(f, delimiter=';')
for row in reader:
    print(row[0],"\t",row[1])