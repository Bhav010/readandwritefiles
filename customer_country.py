import csv

# customers_file = open("customers.csv", "r")
# print(customers_file.read())
# customers_file.close()

with open("customers.csv", "r") as file1:
    read1 = csv.reader(file1)

    with open("customer_country.csv", "w", newline="") as file2:
        write1 = csv.writer(file2)

        select_col = [1, 2, 4]

        for row in read1:
            content = list(row[i] for i in select_col)
            write1.writerow(content)
