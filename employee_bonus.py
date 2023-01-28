import csv

with open("EmployeePay.csv", "r") as file:
    read = csv.reader(file)
    for row in read:
        print(row)
