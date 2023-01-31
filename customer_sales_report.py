import csv

with open("sales.csv", "r") as file1:
    with open("salesreport.csv", "w") as file2:
        write1 = csv.writer(file2)
        read1 = csv.reader(file1)
        next(read1, None)
        var1 = 0
        var2 = 0
        write1.writerow(["Customerid", "Total"])
        for row in read1:
            cal_total = float(row[3]) + float(row[4]) + float(row[5])
            if row[0] != var1:
                if var1 != 0:
                    write1.writerow([var1, var2])
                var1 = row[0]
                var2 = cal_total
            else:
                var2 = var2 + cal_total
        write1.writerow([var1, var2])
