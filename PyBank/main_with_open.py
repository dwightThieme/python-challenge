"""
This script analyzes a financial data set and returns the following statistics:

1) The total number of months included in the dataset
2) The net total amount of "Profit/Losses" over the entire period
3) The average of the changes in "Profit/Losses" over the entire period
4) The greatest increase in profits (date and amount) over the entire period
5) The greatest decrease in losses (date and amount) over the entire period

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

# Import csv and os libraries to read/write
# csv files and simplify file path creation
import csv
import os

# Assemble the output resource path. Include the base and
# repo paths to allow for both absolute and relative paths
# There are various ways to do this

# Use the tradintional Windows '\' path separator first. If
# the shell is set to Bash on a Windows machine, the path
# strings must be prefaced with an 'r' (raw string) so that
# the '\' is correctly interpreted as a path separator and
# not the Bash (Linux) escape character, '\' (This is what
# is causing the problem.) Alternatively, preface the Windows
# path separator character with the Linux OS escape charater,
# i.e., use '\\' instead of '\' (the uglier workaround, IMHO)

base_path = r"C:\Users\dwigh"
repo_path = r"Desktop\Repositories\python-challenge\PyBank"
resource_path = r"Resources\budget_data.csv"
input_path = os.path.join(base_path, repo_path, resource_path)

# This the vanilla Windows path string ('\' path separator)
# Note: Must specify a raw string! Do so with an 'r' prefix
print(f"\nWindows OS Style: \n{input_path}")

# Easy way to switch out OS path separator characters
input_path = input_path.replace("\\", "/")

# Windows treats '/' as a valid separator character when found
# in a path string, i.e., '/' is a univeral OS path separator
print(f"\nUniversal OS Style: \n{input_path}")

# Assemble the output resource path, this time
# using the '/' as the path separator
base_path = "C:/Users/dwigh"
repo_path = "Desktop/Repositories/python-challenge/PyBank"
resource_path = "Resources/budget_data.csv"
input_path = os.path.join(base_path, repo_path, resource_path)

# If '\' and '/' are used in the same path string, Windows
# will recognize both as valid separator characters:
print(f"\nMixed OS Style: \n{input_path}")

# Assemble the input csv file path, starting from the cwd
input_path = os.path.join(os.path.dirname(__file__), "Resources", "budget_data.csv")

# Open the budget_data csv file for reading
with open(input_path, encoding="utf-8", newline="") as csvfile:
    # with open(budget_data, newline="") as csvfile:

    csvread = csv.reader(csvfile, delimiter=",")

    # Note: It is better to make the initializiation
    # of the variables used in this analysis explicit
    # by processing the next two rows of data separately
    # rather than implicitly by processing them as part
    # of the loop

    # Skip header row since it has no data values and
    # read the next record
    next(csvread)
    record = next(csvread)

    # Get the current amount and initialize all variables dependent
    # on a single monrh of data -- the first and total amounts --
    # which will be the same for the first month
    current_amt = int(record[1])
    first_amt = total_amt = current_amt

    # Set the current amount to be next month's previous amount
    # so that monthly differentials can be calculated
    previous_amt = current_amt

    # Go to the next record, initialize the monthly differental and month
    # count variables, and update the previously initialized variables
    record = next(csvread)

    month_count = 2
    current_amt = int(record[1])
    total_amt += current_amt

    # Calculate the montly change in profits and initialize the max increase
    # and decrease variables, which will be the same for the second month
    amt_diff = current_amt - previous_amt
    max_incr = max_decr = amt_diff

    # The same is true for the max increase and decrease dates
    max_incr_date = max_decr_date = record[0]

    # Set current_amt to be next month's previous_amt
    previous_amt = current_amt

    # Loop through the remaining records once all
    # analysis variables have been initialized
    for record in csvread:
        month_count += 1
        current_amt = int(record[1])
        total_amt += current_amt
        amt_diff = current_amt - previous_amt

        # After the second month, update the max profit stats whenever a
        # monthly incr/decr is greater than the stored max incr/decr amounts

        if amt_diff > max_incr:
            max_incr = amt_diff
            max_incr_date = record[0]

        if amt_diff < max_decr:
            max_decr = amt_diff
            max_decr_date = record[0]

        # Next month's previous amount is this month's current amount
        previous_amt = current_amt

# Once the total number of months is known, calculate the average montly
# amount change. For n months, the number of monthly amount changes is n-1
avg_diff = (current_amt - first_amt) / (month_count - 1)

# Create the financial analysis report text
report = (
    f"{' Financial Analysis ':-^48}\n"
    f"{'Total Months:':24}{month_count:24,.0f}\n"
    f"{'Net Profits:':24}{total_amt:24,.0f}\n"
    f"{'Avg Change:':24}{avg_diff:24,.0f}\n"
    f"{'Max Increase:':14}{max_incr_date:^20}{max_incr:14,.0f}\n"
    f"{'Max Decrease:':14}{max_decr_date:^20}{max_decr:14,.0f}\n"
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
