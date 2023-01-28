import csv

with open("sales.csv", "r") as file1:
    read1 = csv.reader(file1)
    for row in read1:
        print(row)
