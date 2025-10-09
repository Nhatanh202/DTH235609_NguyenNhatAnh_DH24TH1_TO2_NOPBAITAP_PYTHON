import csv
with open('Baitap chuong_7/Cau 6/datacsv.csv', mode='r') as f:
    reader = csv.reader(f, delimiter=';')
    for row in reader:
        print(row[0],"\t",row[1])   