#Import the os and module for reading CSV file
import os
import csv

    
total_month = 0
total = 0

profit_loss = []
date = []
month = []
preceding_row = None

# create lists and append values from each row to the list

#Establish CSV path
#csvpath = "C:\\Users\\obrie\\GWARL201811DATA3\\02-Homework\\03-Python\\Instructions\\PyBank\\Resources\\budget_data.csv"
csvpath = os.path.join('..', 'Resources', 'budget_data.csv')

#Read file using CSV module
with open(csvpath) as csvfile:
    
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    
    next(csvreader, None) 
    for row in csvreader:
        
         # Total number of months included in the dataset
        total_month = total_month + 1
        
        # Total net amount of "Profit/Losses" over the entire period
        total += int(row[1])
        
        # Average change in "Profit/Losses" between months over the entire period
        # all_profit_net = str(total / total_month)
    
        first_row = next(csvreader)
        if not (preceding_row):
            preceding_row = int(first_row[1])
        net_change = preceding_row - int(row[1]) 
        profit_loss.append(net_change)
        preceding_row = int(row[1])

        # Greatest increase in profits (date and amount) over the entire period
        max_profit_loss = max(profit_loss)
        
        # Greatest decrease in losses (date and amount) over the entire period
        min_profit_loss = min(profit_loss)
  
    print("Total Months: " + str(total_month))
    print("Net Profit & Loss: $" + str(total))
    print("First Net Change: " + str(profit_loss[0]))
    print("Greatest Increase in Profits: " + str(max_profit_loss))
    print("Greatest Decrease in Profits: " + str(min_profit_loss))


# =============================================================================
# profit_loss = []
# date = []
# profit_loss_change = []
#     
# for i in range(1,len(profit_loss)):
#         profit_loss_change.append(profit_loss[i] - profit_loss[i-1]) 
#         
#         avg_profit_loss_change = sum(profit_loss_change)/len(profit_loss_change)
# 
#         max_profit_loss_change = max(profit_loss_change)
# 
#         min_profit_loss_change = min(profit_loss_change)
# 
#         max_profit_loss_change_date = str(date[profit_loss_change.index(max(profit_loss_change))])
#         min_profit_loss_change_date = str(date[profit_loss_change.index(min(profit_loss_change))])
# 
# print("Average Profit and Loss Change: $", round(avg_profit_loss_change))
# print("Greatest Increase in Profits:", max_profit_loss_change_date,"($", max_profit_loss_change,")")
# print("Greatest Decrease in Profits:", min_profit_loss_change_date,"($", min_profit_loss_change,")")
# 
#     
# 
# =============================================================================
