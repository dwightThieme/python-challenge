"""
This script analyzes a financial data set and returns the following statistics:

1) The total number of months included in the dataset
2) The net total amount of "Profit/Losses" over the entire period
3) The average of the changes in "Profit/Losses" over the entire period
4) The greatest incr in profits (date and amount) over the entire period
5) The greatest decr in losses (date and amount) over the entire period

All statistics are calculated concurrent with a single pass through the data.
Only string and numeric type variables are used; mutable data types (lists
and dictionaries) are not needed since all parameters are known in advance.
When calculating the average change in monthly amounts, the monthly amount
differences are not summed before dividing by their total number. Since the
first monthly amount change is amt2 - amt1, the second amt3 - amt2, the third
amt4 - amt3, etc., all but the first and last monthly amounts cancel when
they are added together, reducing their sum to the first monthly amount
subtracted from the last monthly amount. This method for summing the monthly
amount changes is preferred since it requires only one operation no matter
how many are added together. The standard computation would have required
approximately twice as many operations as there were monthly amount changes.
"""

# Import csv methods to read/write csv files
import csv

# Import os methods to construct valid file paths for the OS
import os

# Assemble the input file path
base_path = 'C:/Users/dwigh'
repo_path = 'Desktop/Repositories/python-challenge/PyBank'
resource_path = 'Resources/budget_data.csv'
input_path = os.path.join(base_path, repo_path, resource_path)

# Open the budget data csv file for reading
with open(input_path, newline='') as csvfile:
    csvread = list(csv.reader(csvfile, delimiter=','))[1:]

month = [row[0] for row in csvread]
month_count = len(month)

profit = [int(row[1]) for row in csvread]
net_profit = sum(profit)

change = [profit[i] - profit[i-1] for i in range(1, month_count)]
max_incr = max(change)
max_decr = min(change)

print(f"\n\n{'max_incr:':11}{max_incr:11,}\
\n{'max_decr:':11}{max_decr:11,}\
\n{'net_profit:':11}{net_profit:11,}\n\n")
