# Import csv methods to read from/write to csv files
import csv

# Import os methods to simplify file path creation
import os

base_path = 'C:/Users/dwigh/Desktop/python-challenge'
resource_path = 'PyBank/Resources/budget_data.csv'
file_path = os.path.join(base_path, resource_path)

# The month_count value conditionally determines how the data is processed
month_count = -1

with open(file_path, newline='') as csvfile:
    csvrecord = csv.reader(csvfile, delimiter=',')

    for record in csvrecord:

        # The first time through the loop the month count is set to zero
        month_count += 1

        # The month count evaluates to False if it is zero, which
        # implies the header row; skip it and go to the next record
        if month_count:

            # The month count evaluates to True for values greater
            # than zero, which implies data that can be processed
            current_amt = int(record[1])

            # Initialize previous and total amounts the first month
            if month_count == 1:
                previous_amt = total_amt = current_amt

            else:
                total_amt += current_amt

                # Calculate montly amount changes after the first month
                amt_change = current_amt - previous_amt

                # Initialize the rest of the variables the second month
                if month_count == 2:
                    max_profit_date = max_loss_date = record[0]
                    max_profit = max_loss = amt_change

                # Check to see if the maximum monthly profit variable
                # values need to be updated after the second month
                elif amt_change > max_profit:
                    max_profit_date = record[0]
                    max_profit = amt_change

                # Check to see if the maximum monthly loss variable
                # values need to be updated after the second month
                elif amt_change < max_loss:
                    max_loss_date = record[0]
                    max_loss = amt_change

                # if month_count > 1:
                #     print(month_count, '  ', record[0], '  ', total_amt, '  ',
                #             previous_amt, '  ', current_amt, '  ', amt_change,
                #             '  ', max_profit_date, '  ', max_profit, '  ',
                #             max_loss_date, '  ', max_loss)

                # This month's current amount will be next month's previous
                # amount if there are more records to be read
                previous_amt = current_amt