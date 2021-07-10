import os
import csv

budget_csv = '/Users/bethanymorton/Desktop/python-challenge/PyBank/Resources/budget_data.csv'

#my data set is long so leave open brackets to put data into
total_m = []
total_pl = []
mpl_change = []

with open(budget_csv) as budgetfile:
    budget_reader = csv.reader(budgetfile, delimiter=",")

    budget_header = next(budget_reader)
    

    for row in budget_reader:
        total_m.append(row[0])

        #gotta convert to an 'int' from 'str'
        total_pl.append(int(row[1]))

    #account for subtraction of header
    #len() will consider all values in specific row iteration
    #set i = individual total-pl values throughout the length of entire row[1] range of data set
    #i+1 for the subsequent value in order to calculate difference
    for i in range(len(total_pl)-1):
        mpl_change.append(total_pl[i+1]-total_pl[i])

greatest_increase_value = max(mpl_change)
greatest_decrease_value = min(mpl_change)

# #index() returns the index of the specified element in the list
# #+1 accounts for the subsequent month associated with that value change
gi_month = mpl_change.index(max(mpl_change))+1
gd_month = mpl_change.index(min(mpl_change))+1

print("Financial Analysis")
print(f"Total Months: {len(total_m)}")
print(f"Total: ${sum(total_pl)}")
print(f"Average Change: {round(sum(mpl_change)/len(mpl_change),2)}")
print(f"Greatest Increase in Profits: {total_m[gi_month]} ${(str(greatest_increase_value))}")
print(f"Greatest Decrease in Profits: {total_m[gd_month]} ${(str(greatest_decrease_value))}")




    
  







    

