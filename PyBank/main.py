# Import csv methods to read from/write to csv files
import csv

# Import os methods to simplify file path creation
import os

base_path = 'C:/Users/dwigh/Desktop/python-challenge'
resource_path = 'PyBank/Resources/budget_data.csv'
file_path = os.path.join(base_path, resource_path)

# Data processing is conditioned on the month count variable alues
month_count = 0

with open(file_path, newline='') as csvfile:
    csvrecord = csv.reader(csvfile, delimiter=',')

    # Skip header row
    next(csvrecord)

    for record in csvrecord:

        # Update the month count and the current amount
        month_count += 1
        current_amt = int(record[1])

        # Initialize previous and total amount values the first month
        if month_count == 1:
            previous_amt = total_amt = current_amt

        # Otherwise update the total and monthly difference values
        else:
            total_amt += current_amt
            difference = current_amt - previous_amt

        # Initialize the remaining variable values the second month
        if month_count == 2:
            max_profit_date = max_loss_date = record[0]
            max_profit = max_loss = difference

        # After the second month, check to see if the maximum monthly
        # profit or loss variable values need to be updated
        if month_count >= 3:

            if difference > max_profit:
                max_profit_date = record[0]
                max_profit = difference

            if difference < max_loss:
                max_loss_date = record[0]
                max_loss = difference

            print(month_count, '  ', record[0], '  ', previous_amt, '  ',
                  current_amt, '  ', difference, '  ', max_profit_date, '  ',
                  max_profit, '  ', max_loss_date, '  ', max_loss, '  ',
                  total_amt)

        # This month's current amount will be next month's previous amount
        previous_amt = current_amt