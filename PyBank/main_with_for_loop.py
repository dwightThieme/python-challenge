"""
This script analyzes a financial data set and returns the following statistics:

1) The total number of months included in the dataset
2) The net total amount of "Profit/Losses" over the entire period
3) The average of the changes in "Profit/Losses" over the entire period
4) The greatest incr in profits (date and amount) over the entire period
5) The greatest decr in losses (date and amount) over the entire period

All statistics are calculated concurrent with a single pass through the data.
Only string and numeric type variables are used; mutable data types (lists
and dictionaries) are not needed since all variables are known in advance.
When calculating the average change in monthly amounts, the monthly amount
differences are not summed before dividing by their total number. Since the
first monthly amount change is amt2 - amt1, the second amt3 - amt2, the third
amt4 - amt3, etc., all but the first and last monthly amounts cancel when
they are added together, reducing their sum to the first monthly amount
subtracted from the last monthly amount. This method for summing the monthly
amount changes is preferred since it the calculation is the same no matter
how many monthly amount changes there are while the usual way of findging
averages requires more calculation the number of monthly changes increases.
"""

# Import csv methods to read/write csv files
import csv

# Import os methods to construct valid file paths for the OS
import os

# Assemble the output resource path. Include the base and
# repo paths to allow for both absolute and relative paths
base_path = 'C:/Users/dwigh'
repo_path = 'Desktop/Repositories/python-challenge/PyBank'
resource_path = 'Resources/budget_data.csv'
input_path = os.path.join(base_path, repo_path, resource_path)

# Open the budget data csv file for reading
with open(input_path, newline='') as csvfile:
    csvread = csv.reader(csvfile, delimiter=',')

    # Process the records in the data file
    for record in csvread:

        # If the current record is the header, no data can be read and
        # month_count is the only variable that can be initialized
        if record[0] == "Date":
            month_count = 0

        # Otherwise the current record has meaningful data to process
        else:

            # Since month_count and current amount are updated every month,
            # they don't need to be incremented/read insided any conditional
            # logic that depends on which month it is
            month_count += 1
            current_amt = int(record[1])

            # At least two months of data are needed to calculate monthly
            # changes, so only first_amt and total_amt can be initialized
            if month_count == 1:
                first_amt = total_amt = previous_amt = current_amt

            # Monthly chages can be calculated after the first month, so
            # initialize the remaining variables and update the rest
            else:

                total_amt += current_amt
                amt_diff = current_amt - previous_amt

                # Initialize the remaining variables the second month ...
                if month_count == 2:

                    max_incr_date = max_decr_date = record[0]
                    max_incr = max_decr = amt_diff

                # ... and after the second month, check to see if
                # the max profit/loss stats need to be updated
                else:

                    if amt_diff > max_incr:

                        max_incr_date = record[0]
                        max_incr = amt_diff

                    if amt_diff < max_decr:

                        max_decr_date = record[0]
                        max_decr = amt_diff

            # After the current record has been processed, set the
            # previous amount to the current amount for next month
            previous_amt = current_amt

# The total number of months is not known until all the records have
# been read. For n months, the number of monthly amount changes is n-1
avg_diff = (current_amt - first_amt) / (month_count - 1)

# Create the financial analysis report text
report = f"{' Financial Analysis ':-^48}\n"                             \
         f"{'Total Months:':24}{month_count:24,.0f}\n"                  \
         f"{'Net Profits:':24}{total_amt:24,.0f}\n"                     \
         f"{'Avg Change:':24}{avg_diff:24,.0f}\n"                       \
         f"{'Max Increase:':14}{max_incr_date:^20}{max_incr:14,.0f}\n"  \
         f"{'Max Decrease:':14}{max_decr_date:^20}{max_decr:14,.0f}\n"  \
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
