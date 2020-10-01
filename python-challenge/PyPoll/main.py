## PyPoll
import os
import csv

##file path
electFilePath = os.path.join("analysis","election_data.csv")

# * In this challenge, you are tasked with helping a small, rural town modernize its vote counting process.

# * You will be give a set of poll data called [election_data.csv](PyPoll/Resources/election_data.csv). 
# The dataset is composed of three columns: `Voter ID`, `County`, and `Candidate`. 
# Your task is to create a Python script that analyzes the votes and calculates each of the following:
      
## list variables
Candidate = []
Votes = []


with open(electFilePath, newline ='') as file:
    csv_reader = csv.reader(file, delimiter =",")
    header = next(csv_reader)
    
    
    for row in csv_reader: 
        vVotes =int(row[0])
        vCandidate =row[2]
 
 #append candidate and votes to a lists           
        Candidate.append(vCandidate)
        Votes.append(vVotes)
  
## cadidate lists      
    vKhan =[]
    vCorrey =[]
    vLi =[]
    vOTooley = []     
         
    for Candidate in Candidate:
        if Candidate =="Khan":
            vKhan.append(Candidate)
        elif Candidate == "Correy":
            vCorrey.append(Candidate)
        elif Candidate == "Li":
            vLi.append(Candidate)
        else: 
            vOTooley.append(Candidate)
              
               
print ("Election Results")
print ("-------------------------")
#   * The total number of votes cast
cntVote = len(Votes)
print(f"Total Votes: {cntVote}")
print ("-------------------------")
    
# A complete list of candidates who received votes 
# The percentage of votes each candidate won
# The total number of votes each candidate won

cntKhan = len(vKhan)
perKhan = round((cntKhan/cntVote) * 100,3)

cntCorrey = len(vCorrey)
perCorrey = round((cntCorrey/cntVote) * 100,3)

cntLi = len(vLi)
perLi = round((cntLi/cntVote) * 100,3)

cntOTooley = len(vOTooley)
perOTooley= round((cntOTooley/cntVote) * 100,3)

if cntKhan > max(cntCorrey, cntLi, cntOTooley):
   winner ="Khan"
elif cntCorrey > max(cntKhan, cntLi, cntOTooley):
    winner = "cntCorrey"
elif cntLi > max(cntKhan, cntCorrey, cntOTooley):
    winner = "Li"
else: 
    winner="O'Tooley"


print(f"Khan: {perKhan} % ({cntKhan})")
print(f"Correy: {perCorrey} % ({cntCorrey}) ")
print(f"Li: {perLi} % ({cntLi})")
print(f"O'Tooley: {perOTooley} % ({cntOTooley})")
print ("-------------------------")
    
#   * The winner of the election based on popular vote.
print(f"Winner: {winner}")

writeOutput = open("analysis\output.txt", "w")
writeOutput.write("Election Results \n" )
writeOutput.write("------------------------- \n")
writeOutput.write(f"Total Votes: {cntVote}\n")
writeOutput.write("------------------------- \n")
writeOutput.write(f"Khan: {perKhan} % ({cntKhan}) \n")
writeOutput.write(f"Correy: {perCorrey} % ({cntCorrey}) \n")
writeOutput.write(f"Li: {perLi} % ({cntLi})\n")
writeOutput.write(f"O'Tooley: {perOTooley} % ({cntOTooley}) \n")
writeOutput.write("------------------------- \n")
writeOutput.write(f"Winner: {winner}\n")

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
