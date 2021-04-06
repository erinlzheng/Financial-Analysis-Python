import os
import csv
#set path to resources and define csvreader and header
PyBankcsv = os.path.join('Resources', 'budget_data.csv')
with open(PyBankcsv,'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    header = next(csvreader)

    #create empty lists
    num_months = []
    profit = []
    change_profit = []
    
                      
    #add values to the list 
    for row in csvreader:
        num_months.append(row[0])
        profit.append(int(row[1]))
    for x in range(1,len(profit)):
        change_profit.append(profit[x]-profit[x-1])
                      
#evaluate the max and min from the list made
increase = max(change_profit)
decrease = min(change_profit)

#delegate month increase and month decrease
month_inc = change_profit.index(max(change_profit))+1
month_dec = change_profit.index(min(change_profit))+1


print("Financial Analysis")
print("------------------------")
print(f"Total Months:{len(num_months)}")
print(f"Total: ${sum(profit)}")
print(f"Average Change: {round(sum(change_profit)/len(change_profit),2)}")
print(f"Greatest Increase in Profits: {num_months[month_inc]} (${(str(increase))})")
print(f"Greatest Decrease in Profits: {num_months[month_dec]} (${(str(decrease))})")      

#set path to analysis folder and write text into text file
PyBankAnalysis = os.path.join('Analysis', 'text file')
with open(PyBankAnalysis,'w') as text:
    text.write("Financial Analysis  \n")
    text.write("------------------------ \n")
    text.write(f"Total Months:{len(num_months)} \n")
    text.write(f"Total: ${sum(profit)} \n")
    text.write(f"Average Change: {round(sum(change_profit)/len(change_profit),2)} \n")
    text.write(f"Greatest Increase: {num_months[month_inc]} (${(str(increase))}) \n")
    text.write(f"Greatest Decrease: {num_months[month_dec]} (${(str(decrease))}) \n")      
