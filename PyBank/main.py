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
    csvread = csv.reader(csvfile, delimiter=',')

    # Data processing is conditioned on the month count parameter
    month_count = 0

    # Skip header row since it has no data values
    next(csvread)

    # Process the records in the data file
    for record in csvread:

        # Update the month count and the current amount
        month_count += 1
        current_amt = int(record[1])

        # Initialize first and total amount parameters the first month
        if month_count == 1:
            first_amt = total_amt = current_amt

        # Otherwise update the total and monthly delta_amt values
        # and initialize/update the remaining parameters
        else:

            total_amt += current_amt
            delta_amt = current_amt - previous_amt

            # Initialize the remaining parameters the second month ...
            if month_count == 2:

                max_incr_date = max_decr_date = record[0]
                max_incr = max_decr = delta_amt

            # ... and after the second month, check to see if
            # the max profit/loss stats need to be updated
            else:

                if delta_amt > max_incr:

                    max_incr_date = record[0]
                    max_incr = delta_amt

                if delta_amt < max_decr:

                    max_decr_date = record[0]
                    max_decr = delta_amt

        # Set the previous amount for next month to this month's current amount
        previous_amt = current_amt

# The total number of months is not known until all the records have
# been read. For n months, the number of monthly amount changes is n-1
avg_delta = (current_amt - first_amt) / (month_count - 1)

# Assemble the output file path
resource_path = 'Resources/budget_analysis.txt'
output_path = os.path.join(base_path, repo_path, resource_path)

# Open the analysis results text file for writing
with open(output_path, 'w+') as txtfile:

    txtfile.write(f"{' Financial Analysis ':-^58}\n")

    txtfile.write(f"{'Total Months:':46}{month_count:12}\n")

    txtfile.write(f"{'Net Amount of Profits/Losses:':46}{total_amt:12,.0f}\n")

    txtfile.write(f"{'Average Monthly Profit/Loss change:':46}")
    txtfile.write(f"{avg_delta:12,.0f}\n")

    txtfile.write(f"{'Greatest Monthly Increase in Profits:':38}")
    txtfile.write(f"{max_incr_date:8}{max_incr:12,.0f}\n")

    txtfile.write(f"{'Greatest Monthly Increase in Losses:':38}")
    txtfile.write(f"{max_decr_date:8}{max_decr:12,.0f}\n")

    txtfile.write(f"{'--':-^58}\n")

# Set the input path to the output path to open the text file for reading
input_path = output_path

# Read the budget analysis report and print it to the terminal
with open(input_path, 'r') as txtfile:
    report = txtfile.read()
    print(f"\n\n{report}\n")
