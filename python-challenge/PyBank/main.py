# * Your task is to create a Python script that analyzes the records to calculate each of the following:
import os
import csv


# Import budget_data.csv
budget_path = os.path.join('analysis', 'budget_data.csv')

#list to store data
vTotal = []
vMonths = []
#Open file and loop through the csv file
with open(budget_path) as csvfile:
# Split the data on commas
    csv_reader = csv.reader(csvfile, delimiter=',')
    
#Count the rows excluding the header
    header = next(csv_reader)
    if header != None: 
        for row in csv_reader: 
            vAmount = int(row[1])
            vMonth = row[0]
            vTotal.append(vAmount) 
            vMonths.append(vMonth)
print("Financial Analysis")
print("----------------------------------------")
#The total number of months included in the dataset
cntMonth = len(vMonths)
print(f"Total Months: {cntMonth}")
# * The net total amount of "Profit/Losses" over the entire period
Total = sum(vTotal)
print(f"Total: ${Total}")

writeOutput = open("output.txt", "w")
writeOutput.write("Financial Analysis \n" )
writeOutput.write("----------------------------------------\n")
writeOutput.write(f"Total Months: {cntMonth} \n")
writeOutput.write(f"Total: ${Total} \n")


# append change data in vChange list
def avgChange(lst_data,lst_mo):
     lstChange = [lst_data[i + 1] - lst_data[i] for i in range(len(lst_data)-1)] 
     vChange = round(sum(lstChange)/len(lstChange),2)

#   * The average of the changes in "Profit/Losses" over the entire period   
     print(f"Average Change: ${vChange}")
     
     lstMonths = []
     for i in lst_mo:
         lstMonths.append(i)
     
     #print(lstChange)    
     lstMonths.pop(0)  
     #print(newListMonth)
     dictList = dict(zip(lstMonths, lstChange))
     key_list = list(dictList.keys()) 
     val_list = list(dictList.values())
     #   * The greatest increase in profits (date and amount) over the entire period
     maxIncrease = max(lstChange)
     maxkeyDate = key_list[val_list.index(maxIncrease)]
     print(f"Greatest Increase in Profits: {maxkeyDate} (${maxIncrease})")
     
#   * The greatest decrease in losses (date and amount) over the entire period
     minDecrease = min(lstChange)
     minkeyDate = key_list[val_list.index(minDecrease)]
     print(f"Greatest Decrease in Profits: {minkeyDate} (${minDecrease})")
     
    #writeOutput = open("output.txt", "w")
     writeOutput.write(f"Average Change: ${vChange}\n")
     writeOutput.write(f"Greatest Increase in Profits: {maxkeyDate} (${maxIncrease})\n")
     writeOutput.write(f"Greatest Decrease in Profits: {minkeyDate} (${minDecrease})\n")
     
 
## call the function  
avgChange(vTotal,vMonths)

# * As an example, your analysis should look similar to the one below:

#   ```text
#   Financial Analysis
#   ----------------------------
#   Total Months: 86
#   Total: $38382578
#   Average  Change:Average  Change: $-2315.12
#   Greatest Increase in Profits: Feb-2012 ($1926159)
#   Greatest Decrease in Profits: Sep-2013 ($-2196167)
#   ```

# * In addition, your final script should both print the analysis to the terminal and export a text file with the results.
