import os
import csv

budget_csv = '/Users/bethanymorton/Desktop/python-challenge/PyBank/Resources/budget_data.csv'

date = []
profit_loss = []

with open(budget_csv, newline='') as budgetfile:
    budget_reader = csv.reader(budgetfile, delimiter=",")
    headings = next(budget_reader)

    output = []
    for row in budget_reader:
        output.append(row[:])









