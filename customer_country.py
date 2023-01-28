import csv

# customers_file = open("customers.csv", "r")
# print(customers_file.read())
# customers_file.close()

with open("customers.csv", "r") as f:
    r = csv.reader(f, delimiter=",")
    for row in r:
        print(row[1], row[2], "-", row[4])
