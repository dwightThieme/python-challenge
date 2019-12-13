"""
A (partial) Pandas-style solution for PyBank
"""

from statistics import mean as avg
import os
import csv

# Assemble the output resource path. Include the base and
# repo paths to allow for both absolute and relative paths
base_path = 'C:/Users/dwigh'
repo_path = 'Desktop/Repositories/python-challenge/PyBank'
resource_path = 'Resources/budget_data.csv'
input_path = os.path.join(base_path, repo_path, resource_path)

with open(input_path, newline='') as csv_file:

    # Construct a list from the csv.reader object
    csv_list = list(csv.reader(csv_file, delimiter=','))

# Generate a list of valid data by stripping out the header
data = csv_list[1:]

# Construct a list of months and get the month count
months = [row[0] for row in data]
month_count = len(months)

# Construc a list of profits and find the net profit
profits = [int(row[1]) for row in data]
net_profit = sum(profits)

# Construct a list of monthly differences from the list of profits
differences = [profits[i] - profits[i-1] for i in range(1, month_count)]

# Find the average monthly change in profits
avg_diff = avg(differences)

# Find the maximum monthy increase, then reference the months list
# with its difference list index for the date of its occurrence
max_incr = max(differences)
max_incr_date = months[differences.index(max_incr)]

# Find the maximum monthy decrease, then reference the months list
# with its difference list index for the date of its occurrence
max_decr = min(differences)
max_decr_date = months[differences.index(max_decr)]

# Create the financial analysis report text
report = f"{' Financial Analysis ':-^48}\n"\
         f"{'Total Months:':24}{month_count:24,.0f}\n"\
         f"{'Net Profits:':24}{net_profit:24,.0f}\n"\
         f"{'Avg Change:':24}{avg_diff:24,.0f}\n"\
         f"{'Max Increase:':14}{max_incr_date:^20}{max_incr:14,.0f}\n"\
         f"{'Max Decrease:':14}{max_decr_date:^20}{max_decr:14,.0f}\n"\
         f"{'--':-^48}"

# Assemble the output resource path. Include the base and
# repo paths to allow for both absolute and relative paths
resource_path = 'Resources/budget_analysis.txt'
output_path = os.path.join(base_path, repo_path, resource_path)

# Open the analysis resource text file and write the report to it
with open(output_path, "w") as textfile:
    textfile.write(report)

# Check to see if the report exists and is properly formatted:

# The input and output resource paths are the same
input_path = output_path

# Open report text file for reading and print it to the terminal
with open(input_path, "r") as textfile:
    report = textfile.read()

print(f"\n\n{report}\n\n")
