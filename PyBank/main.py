import pandas as pd

# Import files
df = pd.read_csv("../Resources/budget_data_1.csv")
df

df2 = pd.read_csv("../Resources/budget_data_2.csv")
df2


#Append dataframes 
budget_df = df.append(df2)
budget_df

#Do some math
#Total number of months included in the dataset
tc = sum(budget_df["Date"].value_counts() )
# Get total and average
tr = budget_df["Revenue"].sum()
ta = budget_df["Revenue"].median()
#Greatest Increase and Decrease
gi = budget_df["Revenue"].max()
gd = budget_df["Revenue"].min()

#Show the user
print("Financial Analysis")
print("Total Months:  " + str(tc))
print("Total Revenue:  " + str(tr))
print("Average Revenue:  " + str(ta))
print("Greatest Increase:  " + str(gi))
print("Greatest Decrease:  " + str(gd))


#Make an outfile for posterity
outfile = budget_df.to_csv("../Output/pybank_budget.csv")