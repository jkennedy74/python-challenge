import pandas as pd
df = pd.read_csv("../Resources/election_data_1.csv")
df2 = pd.read_csv("../Resources/election_data_2.csv")


poll_data = df.append(df2)

# Get total votes
total_votes = sum(poll_data["Voter ID"].value_counts())
print(total_votes)

# Get complete list of candidates that received votes
all_votes = poll_data['Candidate'].value_counts()
print(all_votes)

pr = all_votes/total_votes*100
print(pr)


winner = all_votes.nlargest(1)
print(winner)
