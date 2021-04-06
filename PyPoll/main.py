import os
import csv

PyPollcsv = os.path.join('Resources', 'election_data.csv')

candidates = []
num_votes = []
percent_votes = []
total_votes = 0

with open(PyPollcsv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    csv_header = next(csvreader)

    for row in csvreader:
    
        total_votes += 1 

    
        if row[2] not in candidates:
            candidates.append(row[2])
            index = candidates.index(row[2])
            num_votes.append(1)
        else:
            index = candidates.index(row[2])
            num_votes[index] += 1
    
     
    for votes in num_votes:
        percentage = (votes/total_votes) * 100
        percentage = round(percentage)
        percentage = "%.3f%%" % percentage
        percent_votes.append(percentage)
    
   
    winner = max(num_votes)
    index = num_votes.index(winner)
    winning_candidate = candidates[index]


print("Election Results")
print("--------------------------")
print(f"Total Votes: {str(total_votes)}")
print("--------------------------")
for i in range(len(candidates)):
    print(f"{candidates[i]}: {str(percent_votes[i])} ({str(num_votes[i])})")
print("--------------------------")
print(f"Winner: {winning_candidate}")
print("--------------------------")


PyPollAnalysis = os.path.join('Analysis', 'text.txt')
with open(PyPollAnalysis,'w') as text:
    text.write = ("Election Results \n")
    text.write = ("-------------------------- \n")
    text.write = str(f"Total Votes: {str(total_votes)} \n")
    text.write = str("-------------------------- \n" )
for i in range(len(candidates)):
    text.write = str(f"{candidates[i]}: {str(percent_votes[i])} ({str(num_votes[i])}) \n")
    text.write = ("--------------------------")
    text.write = str(f"Winner: {winning_candidate} \n")
    text.write = ("-------------------------- \n")
