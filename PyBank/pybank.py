# Dependencies
import os
import csv

# Specify file path
# budget_data_csv = os.path.join("..", "..", "..", "DataVisHomework", "PythonHomework", "PyBank", "budget_data.csv")
path = 'C:\\Users\\dwigh\\Desktop\\python-challenge\\PyBank\\Resources'
resource = 'budget_data.csv'
budget_data_csv = os.path.join(path, resource)
# Open the file. Specify Varialbe to hold the contents as csvfile
with open(budget_data_csv, 'r', newline='') as csvfile:
    
    #parse csv file into dict
    csvreader = csv.DictReader(csvfile) 
    
    #####for row in csvreader:
        #####print(row['Date'], row['Profit/Losses']) - Test output
    
    # count months by row
    row_count = sum(1 for row in csvreader) 
    #####print(row_count) 
    
with open(budget_data_csv, 'r', newline='') as csvfile:
    csvreader = csv.DictReader(csvfile)
    
    #parse 'Profit/Losses' from dict as int in list
    pnl = [int(row['Profit/Losses']) for row in csvreader]
    
    #sum pnl 
    total_pnl = sum(pnl) 
    #####print(total_pnl)

with open(budget_data_csv, 'r', newline='') as csvfile:
    csvreader = csv.DictReader(csvfile)
    
    # parse 'Profit/Losses' from dict as int in list
    data = [int(row['Profit/Losses']) for row in csvreader]
    #####print(data) - Test output

    #get all monthly changes from list
    monthly_change = [data[i] - data[i - 1] for i in range(1, len(data))]
    
    #####print(monthly_change) -Test output
    
    #average monthly change over all months
    average_monthly_change = round(sum(monthly_change)/(row_count - 1), 2) 
    #####print(average_monthly_change) 

    #Get max change in monthly change list
    max_change = max(monthly_change)
    
    #Locate index value of max change
    max_change_location = monthly_change.index(max_change)
    #####print(max_change_location, max_change)

    #Get min change in monthly change list
    min_change = min(monthly_change)
    
    #Locate index value of min change
    min_change_location = monthly_change.index(min_change)
    #####print(min_change_location, min_change)

    
with open(budget_data_csv, 'r', newline='') as csvfile:
    csvreader = csv.DictReader(csvfile)
    
    #parse 'Date' from dict as string in list
    data_date =  [str(row['Date']) for row in csvreader]
    ##### print(data_date) - Test output
    
    #find max change date using index location of max_change_location
    max_change_date = data_date[max_change_location + 1]
    #####print(max_change_date)

    #find min change date using index location of min_change_location
    min_change_date = data_date[min_change_location + 1]
    #####print(min_change_date)

#---------------------------------------------------------------------------

#Output

#print to Terminal
print('')
print('Financial Analysis')
print('---------------------')
print('Total Months: ' + str(row_count))
print('Total: ' + '$ ' + str(total_pnl))
print('Average Change: ' + '$ ' + str(average_monthly_change))
print('Greatest Increase in Profits: ' + str(max_change_date) + ' $ ' + str(max_change))
print('Greatest Decrease in Profits: ' + str(min_change_date) + ' $ ' + str(min_change))
print('')


#print to TextFile
import sys
sys.stdout=open("output.txt","w")
print('')
print('Financial Analysis')
print('---------------------')
print('Total Months: ' + str(row_count))
print('Total: ' + '$ ' + str(total_pnl))
print('Average Change: ' + '$ ' + str(average_monthly_change))
print('Greatest Increase in Profits: ' + str(max_change_date) + ' $ ' + str(max_change))
print('Greatest Decrease in Profits: ' + str(min_change_date) + ' $ ' + str(min_change))
print('')
sys.stdout.close()
