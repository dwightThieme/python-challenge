"""
A (partial) Pandas-style solution for PyBank
"""

from statistics import mean as avg
import os
import csv

# Assemble the output resource path. Include the base and
# repo paths to allow for both absolute and relative paths
base_path = r"C:\Users\dwigh"
repo_path = r"Desktop\Repositories\python-challenge\PyBank"
resource_path = r"Resources\budget_data.csv"
input_path = os.path.join(base_path, repo_path, resource_path)

print(f"\n\nWindows style input path -> \n{input_path}")

# Unix-style path separators are valid in _all_ environments
input_path = input_path.replace("\\", "/")

print(f"\nUnix style input path -> \n{input_path}")

with open(input_path, newline="") as csv_file:

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

# Assemble the output resource path. Include the base and
# repo paths to allow for both absolute and relative paths
resource_path = "Analysis/budget_analysis.txt"
output_path = os.path.join(base_path, repo_path, resource_path)

# Open the analysis resource text file and write the report to it
with open(output_path, "w") as textfile:
    textfile.write(report)

# Check to see if the report exists and is properly formatted:
# The input and output resource paths are the same ... but we
# we strive for clarity!
input_path = output_path

# Open report text file for reading and print it to the terminal
with open(input_path, "r") as textfile:
    report = textfile.read()

print(f"\n\n{report}\n\n")

# amounts = []
# for record in csv_data:
#     amounts.append(int(row[1]))
# for i in range(1, len(months)):
#     print(
#         f"{amounts[i]:14,.0f}"
#         f"{amounts[i-1]:14,.0f}"
#         f"{(amounts[i]-amounts[i-1]):14,.0f}"
#         f"{months[i]:>14}"
#     )
# count = len(months)
# previous_month_amounts = amounts[:count]
# current_month_amounts = amounts[1:]
# differences = []
# for i in range(len(current_month_amounts)):
#     differences.append(current_month_amounts[i] - previous_month_amounts[i])
# for diffs in differences:
#     print(f"{diffs:14,.0f}")
# print(differences)
# for row in csv_data:
#     print(f"{row[0]:8}  {int(row[1]):14,.0f}")
# print(csv_data)
