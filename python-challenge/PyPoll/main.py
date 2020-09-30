## PyPoll
import os
import csv

electFilePath = os.path.join("analysis","election_data.csv")

# * In this challenge, you are tasked with helping a small, rural town modernize its vote counting process.

# * You will be give a set of poll data called [election_data.csv](PyPoll/Resources/election_data.csv). 
# The dataset is composed of three columns: `Voter ID`, `County`, and `Candidate`. 
# Your task is to create a Python script that analyzes the votes and calculates each of the following:
totalVote =[]
vCounty = []
vCandidate = []

with open(electFilePath) as file:
    csv_reader = csv.reader(file, delimiter =",")
    header = next(csv_reader)
    if header != None: 
        for row in csv_reader: 
            voteID = row[0]
            county = row[1]
            candidate = row[2]
                
            totalVote.append(voteID) 
            vCounty.append(county)
            vCandidate.append(candidate)

print ("Election Results\n")
print ("-------------------------\n")

#   * The total number of votes cast
cntVote = len(totalVote)
print(f"Total Votes: {cntVote}\n")
print ("-------------------------\n")
# A complete list of candidates who received votes 
# The percentage of votes each candidate won
# The total number of votes each candidate won

print(f"Khan: \n")
print(f"Khan: \n")
print(f"Khan: \n")
print(f"Khan: \n")
print ("-------------------------\n")

#   * The winner of the election based on popular vote.
print(f"Winner:\n")


# * As an example, your analysis should look similar to the one below:

#   ```text
#   Election Results
#   -------------------------
#  Total Votes: Total Votes: 3521001
#   -------------------------
#   Khan: 63.000% (2218231)
#   Correy: 20.000% (704200)
#   Li: 14.000% (492940)
#   O'Tooley: 3.000% (105630)
#   -------------------------
#   Winner: Khan
#   -------------------------
#   ```

# * In addition, your final script should both print the analysis to the terminal and export a text file with the results.
