"""
This script analyzes an election vote count data set and returns the following:

1) The total number of votes cast
2) A complete list of candidates who received votes
3) The percentage of votes each candidate won
4) The total number of votes each candidate won
5) The winner of the election based on popular vote.

All statistics are calculated concurrent with a single pass through the data.
Since the variables are not known in advance, i.e., the names of the candidates
who are up for election, mutable data types (lists and dictionaries) are used.
"""

# Import csv and os libraries to read/write
# csv files and simplify file path creation
import csv
import os

# Assemble the input csv file path, starting from the cwd
input_path = os.path.join(os.path.dirname(__file__), "Resources", "election_data.csv")

# Open the election_data csv file for reading
with open(input_path, encoding="utf-8", newline="") as csvfile:
    csvread = csv.reader(csvfile, delimiter=",")

    # Skip header row since it is not valid data
    next(csvread)

    # Initialize the vote count dictionary
    votes = {}

    # Loop through the remaining records
    for record in csvread:
        # Get the candidate's name, which is a dictionary key
        candidate = str(record[2])

        # If this is the first the candidate has received a
        # vote, the candidate key and the default value, 0
        # (given by the second argument in the get() method)
        # are added to the dictionary before incrementing the
        # candidates vote count by 1
        votes[candidate] = votes.get(candidate, 0) + 1

# Find the total number of votes
total = sum(votes.values())

# Find the name key of the maximum value in the dictionary
winner = max(votes, key=votes.get)

# Format the votes dictionary entries for the report
lines = [
    f"{k + ':':24}" f"{votes[k]:10,}" f"{votes[k]/total * 100:11,.2f}%\n"
    for k in sorted(votes)
]

# Generate the report string text
report = (
    f"{' Election Results ':^46}\n"
    f"{'--':-^46}\n"
    f"{'Total Votes:':24}{total:10,}{100:11,.2f}%\n"
    f"{'--':-^46}\n"
    f"{''.join(lines)}"
    f"{'--':-^46}\n"
    f"{'Winner:':10}{winner:>24}{votes[winner]/total * 100:11,.2f}%\n"
    f"{'--':-^46}\n"
)

# Assemble the output text file path, starting from the cwd
output_path = os.path.join(os.path.dirname(__file__), "Analysis", "poll_analysis.csv")
print(f"\n\n {output_path} \n\n")

# Open the poll_analysis text file and write the report to it
with open(output_path, "w", encoding="utf-8") as textfile:
    textfile.write(report)

# Check to see if the report exists and is properly formatted:
# The input and output resource paths are the same ... but we
# we strive for clarity!
input_path = output_path

# Open the report text file for reading and print it to the terminal
with open(input_path, "r", encoding="utf-8") as textfile:
    report = textfile.read()

# And print it out to see if the information, formatting, etc. is correct
print(f"\n\n{report}\n\n")
