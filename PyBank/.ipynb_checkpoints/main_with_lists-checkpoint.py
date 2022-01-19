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

    csv_reader = csv.reader(csv_file, delimiter=',')

    # Don't include the csv file header in the data
    header = next(csv_reader)

    # Pass the raw text data out as a list
    csv_data = list(csv_reader)

# Exract the month data and find the month count
months = [row[0] for row in csv_data]
num_months = len(months)

# Extract the profit data and find the net profit
profits = [int(row[1]) for row in csv_data]
net_profits = sum(profits)

# To generate difference data, first get a list of mmonths
# and monthly differences for the second through last months
monthly_differences = [[profits[i] - profits[i-1], months[i]]
                       for i in range(1, num_months)]

# Find the average monthly change in profits
avg_diff = avg(diff[0] for diff in monthly_differences)

# Find the maximum monthy increase and the month in which it occurs
max_incr = max(monthly_differences)

# Find the maximum monthy decrease and the month in which it occurs
max_decr = min(monthly_differences)

# Create the financial analysis report text
report = f"{' Financial Analysis ':-^48}\n"                             \
         f"{'Total Months:':24}{num_months:24,.0f}\n"                   \
         f"{'Net Profits:':24}{net_profits:24,.0f}\n"                   \
         f"{'Avg Change:':24}{avg_diff:24,.0f}\n"                       \
         f"{'Max Increase:':14}{max_incr[1]:^20}{max_incr[0]:14,.0f}\n" \
         f"{'Max Decrease:':14}{max_decr[1]:^20}{max_decr[0]:14,.0f}\n" \
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
