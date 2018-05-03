import os
import csv

# Set path -- why do we need this??
csvpath = os.path.join("../Resources/election_data_1.csv")
csvpath2 = os.path.join("../Resources/election_data_2.csv")

# Lists to store data
voter_id = []
county = []
candidate = []
total_votes = 1

# Read file 1
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    for row in csvreader:
        total_votes = total_votes +1
        voter_id.append(row[0])
        county.append(row[1])
        candidate.append(row[2])


# Read file 2
with open(csvpath2, newline="") as csvfile:
    csvreader2 = csv.reader(csvfile, delimiter=",")

    for row in csvreader2:
        total_votes = total_votes + 1
        voter_id.append(row[0])
        county.append(row[1])
        candidate.append(row[2])



# Zip lists together
cleaned_csv = zip(voter_id, county, candidate)


# Do some math
# Total votes from counter above in reader loops
print(total_votes) 


#Set output file path
output_file = os.path.join("../output/election_data.csv")

#Write to file
with open(output_file, "w", newline="") as datafile:
    writer = csv.writer(datafile)
    writer.writerows(cleaned_csv)

print("Yep, I'm slow.  But I'm done")

