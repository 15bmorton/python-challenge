import os
import csv
from pathlib import Path

election_data = '/Users/bethanymorton/Desktop/python-challenge/PyPoll/Resources/election_data.csv'

vote_total = 0
votes_khan = 0
votes_li = 0
votes_correy = 0
votes_otooley = 0

with open(election_data,newline="", encoding="utf-8") as datafile:
    datareader = csv.reader(datafile, delimiter = ",")

    dataheader = next(datareader)

    for row in datareader:
        vote_total +=1

        if row[2] == "Khan":
            votes_khan +=1
        elif row[2] == "Li":
            votes_li +=1
        elif row[2] == "Correy":
            votes_correy +=1
        elif row[2] == "O'Tooley":
            votes_otooley +=1
      
candidates = ["Khan", "Li", "Correy", "O'Tooley"]
votes = [votes_khan, votes_li, votes_correy, votes_otooley]

cv_dict= dict(zip(candidates,votes))
key = max(cv_dict, key=cv_dict.get)

pct_khan = (votes_khan/ vote_total) *100
pct_li = (votes_li/ vote_total) *100
pct_correy = (votes_correy/ vote_total) *100
pct_otooley = (votes_otooley/ vote_total) *100

print(f"Election Results")
print(f"Total Votes: {vote_total}")
print(f"Khan: {pct_khan:.3f}% ({votes_khan})")
print(f"Correy: {pct_correy:.3f}% ({votes_correy})")
print(f"Li: {pct_li:.3f}% ({votes_li})")
print(f"O'Tooley: {pct_otooley:.3f}% ({votes_otooley})")
print(f"Winner: {key}")

output_file = '/Users/bethanymorton/Desktop/python-challenge/PyPoll/analysis/Election_Results'

with open(output_file,"w") as file:

    file.write(f"Election Results")
    file.write("\n")
    file.write(f"Total Votes: {vote_total}")
    file.write("\n")
    file.write(f"Khan: {pct_khan:.3f}% ({votes_khan})")
    file.write("\n")
    file.write(f"Correy: {pct_correy:.3f}% ({votes_correy})")
    file.write("\n")
    file.write(f"Li: {pct_li:.3f}% ({votes_li})")
    file.write("\n")
    file.write(f"O'Tooley: {pct_otooley:.3f}% ({votes_otooley})")
    file.write("\n")
    file.write(f"Winner: {key}")
    file.write("\n")


