"""
A (partial) Pandas-style solution for PyBank
"""

from statistics import mean as avg
import os
import csv

base_path = 'C:/Users/dwigh'
repo_path = 'Desktop/Repositories/python-challenge/PyBank'
resource_path = 'Resources/budget_data.csv'

input_path = os.path.join(base_path, repo_path, resource_path)

with open(input_path, newline='') as csv_file:
    csv_read = csv.reader(csv_file, delimiter=',')
    csv_list = list(csv_read)

csv_clean = csv_list[1:]

months = [row[0] for row in csv_clean]
month_count = len(months)

profits = [int(row[1]) for row in csv_clean]
net_profit = sum(profits)


differences = [profits[i] - profits[i-1] for i in range(1, month_count)]

avg_diff = avg(differences)

max_incr = max(differences)
max_incr_index = differences.index(max_incr)
max_incr_date = months[max_incr_index]

max_decr = min(differences)
max_decr_index = differences.index(max_decr)
max_decr_date = months[max_decr_index]


report = f"\
\n\n\n\n\
            {' Financial Analysis ':-^48}\n\
            {'Total Months:':24}{month_count:24,.0f}\n\
            {'Net Profits:':24}{net_profit:24,.0f}\n\
            {'Avg Change:':24}{avg_diff:24,.0f}\n\
            {'Max Increase:':14}{max_incr_date:^20}{max_incr:14,.0f}\n\
            {'Max Decrease:':14}{max_decr_date:^20}{max_decr:14,.0f}\n\
            {'--':-^48}\
\n\n\n\n"

print(report)
