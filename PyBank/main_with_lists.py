"""
A (partial) Pandas-style solution for PyBank
"""

from statistics import mean as avg
import os
import csv

# Assemble the input csv file path, starting from the cwd
input_path = os.path.join(os.path.dirname(__file__), "Resources", "budget_data.csv")

# Open the budget_data csv file for reading
with open(input_path, encoding="utf-8", newline="") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    # Don't include the csv file header in the data
    next(csv_reader)

    # Pass the raw text data out as a list
    csv_data = list(csv_reader)

# Exract the month data and find the month count
months = [record[0] for record in csv_data]
num_months = len(months)

# Extract the profit data and find the net profit
profits = [int(record[1]) for record in csv_data]
net_profits = sum(profits)

# To generate difference data, first get a list of mmonths
# and monthly differences for the second through last months
monthly_differences = [
    [months[i], profits[i] - profits[i - 1]] for i in range(1, num_months)
]

# Find the average monthly change in profits
avg_diff = avg(diff[1] for diff in monthly_differences)

# Find the maximum monthy increase and the month in which it occurs
max_incr = max(monthly_differences, key=lambda col: col[1])

# Find the maximum monthy decrease and the month in which it occurs
max_decr = min(monthly_differences, key=lambda col: col[1])

# Create the financial analysis report text
report = (
    f"{' Financial Analysis ':-^48}\n"
    f"{'Total Months:':24}{num_months:24,.0f}\n"
    f"{'Net Profits:':24}{net_profits:24,.0f}\n"
    f"{'Avg Change:':24}{avg_diff:24,.0f}\n"
    f"{'Max Increase:':14}{max_incr[0]:^20}{max_incr[1]:14,.0f}\n"
    f"{'Max Decrease:':14}{max_decr[0]:^20}{max_decr[1]:14,.0f}\n"
    f"{'--':-^48}"
)

# Assemble the output text file path, starting from the cwd
output_path = os.path.join(os.path.dirname(__file__), "Analysis", "budget_analysis.txt")

# Open the budget_analysis text file and write the report to it
with open(output_path, "w", encoding="utf-8") as textfile:
    textfile.write(report)

# Check to see if the report exists and is properly formatted:
# The input and output resource paths are the same ... but we
# we strive for clarity!
input_path = output_path

# Open the report text file for reading and print it to the terminal
with open(input_path, "r", encoding="utf-8") as textfile:
    report = textfile.read()

print(f"\n\n{report}\n\n")
