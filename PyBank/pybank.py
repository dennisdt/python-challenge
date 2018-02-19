# PyBank Assignment

import csv

file_path = "raw_data/budget_data_1.csv"

count = 0

with open(file_path) as csv_data:
    reader = csv.DictReader(csv_data)

    for row in reader:
        count = count + 1
        print(row["Date"])
        print(row['Revenue'])

print("the number of rows is: " + str(count))