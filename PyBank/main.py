"""
This script analyzes a financial data set and returns the following statistics.

1: The total number of months included in the dataset
2: The net total amount of "Profit/Losses" over the entire period
3: The average of the changes in "Profit/Losses" over the entire period
4: The greatest incr in profits (date and amount) over the entire period
5: The greatest decr in losses (date and amount) over the entire period

The data is read once and stored in string and numeric variables; lists and
dictionaries are not needed and not used. Also, since the first monthly change
is amt2 - amt1, the second is amt3 - amt2, the third is amt4 - amt3, etc., all
but the first and last monthly amounts cancel when summed together, reducing
the sum of the monthly change in amounts to the first monthly amount
the first monthly amount. This is far more computationally efficient than
calculating every change in monthly amounts before summing them.
"""

# Import csv methods to read from/write to csv files
import csv
# Import os methods to simplify file path creation
import os

base_path = 'C:/Users/dwigh/Desktop/python-challenge'
resource_path = 'PyBank/Resources'

#  the budget data from a record resource file
input_path = os.path.join(base_path, resource_path, 'budget_data.csv')

# Data processing is conditioned on the month count variable values
month_count = 0

with open(input_path, newline='') as csvfile:
    csvread = csv.reader(csvfile, delimiter=',')

    # Skip header row
    next(csvread)

    for record in csvread:

        # Update the month count and the current amount
        month_count += 1
        current_amt = int(record[1])

        # Initialize previous and total amount values the first month
        if month_count == 1:
            previous_amt = first_amt = total_amt = current_amt

        # Otherwise update the total and monthly delta_amt values
        else:
            total_amt += current_amt
            delta_amt = current_amt - previous_amt

        # Initialize the remaining variable values the second month
        if month_count == 2:
            max_incr_date = max_decr_date = record[0]
            max_incr = max_decr = delta_amt

        # After the second month, update the max profit stats if the latest
        # monthly incr/decr is greater than the current max incr/decr amounts
        if month_count > 2:

            if delta_amt > max_incr:
                max_incr_date = record[0]
                max_incr = delta_amt

            if delta_amt < max_decr:
                max_decr_date = record[0]
                max_decr = delta_amt

        # Next month's previous amount is this month's current amount
        previous_amt = current_amt

# The total number of months is not known until all the records have
# been read. For n months, the number of monthly changes is n-1
avg_delta = (current_amt - first_amt) / (month_count - 1)

# Write the results of the analysis to a report resource file
output_path = os.path.join(base_path, resource_path, 'budget_analysis.txt')

with open(output_path, 'w+') as txtfile:
    txtfile.write(' ' * 21 + "Financial Analysis" + '\n')
    txtfile.write('-' * 60 + '\n')
    txtfile.write("{0:58}{1}".format(
                  "Total Months:", month_count) + '\n')
    txtfile.write("{0:49}${1:,}".format(
                  "Total Amount:", total_amt) + '\n')
    txtfile.write("{0:53}-${1:,.0f}".format(
                  "Average Monthly Change in Profit:",
                  abs(avg_delta)) + '\n')
    txtfile.write("{0:38}{1:10}  ${2:,}".format(
                  "Greatest Monthly Increase in Profit:",
                  max_incr_date, max_incr) + '\n')
    txtfile.write("{0:38}{1:10} -${2:,}".format(
                  "Greatest Monthly Decrease in Profit:",
                  max_decr_date, abs(max_decr)))

input_path = os.path.join(base_path, resource_path, 'budget_analysis.txt')

# Check the report file to make sure it was correctly generated
with open(input_path, 'r') as txtfile:
    report = txtfile.read()
    print(report)
