import os
import csv

budget_csv = os.path.join("Resources", "budget_data.csv")

# Open and read csv
with open(budget_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Read the header row first (skip this part if there is no header)
    csv_header = next(csvreader)
    print(f"Header: {csv_header}")

    # Read through each row of data after the header
    monthCounter = 0
    netTotalPL = 0
    for row in csvreader:

        monthCounter += 1
        netTotalPL += int(row[1])
        
        


    print(monthCounter)
    print(netTotalPL)
 