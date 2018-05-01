import os
import csv



# Lists to store the data
month = []
revenue = []

path = os.path.join("../Resources", "budget_data_1.csv")


with open(path, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    for row in csvreader:
        month.append(row[0])
        revenue.append(row[1])

# Zip lists together
scrubbed = zip(month, revenue)

outfile = os.path.join("budget_data.csv")

with open(outfile, "w", newline="") as datafile:
    writer = csv.writer(datafile)

    # Don't need the line below.  Data already has headers.
    # writer.writerow(["Month", "Revenue"])

    writer.writerows(scrubbed)

