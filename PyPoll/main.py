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

# Construct the input resource path. Include the base path
# to allow for absolute as well as relative paths
# repo paths to allow for both absolute and relative paths
base_path = 'C:/Users/dwigh'
repo_path = 'Desktop/Repositories/python-challenge/PyPoll'
resource_path = 'Resources/election_data.csv'
input_path = os.path.join(base_path, repo_path, resource_path)

# Open the election data csv file for reading
with open(input_path, newline="") as csvfile:

    csvread = csv.reader(csvfile, delimiter=",")

    # Skip header row since it is not valid data
    next(csvread)

    # Initialize the vote count dictionary
    votes = {}

    # Loop through the remaining records
    for record in csvread:

        # Get the candidate's name, which is a dictionary key
        candidate = str(record[2])

        # Increment the candidate's count by 1. If this is the
        # first time the candidate has received a vote, add the
        # candidate key and default vote (0) to the dictionary
        votes[candidate] = votes.get(candidate, 0) + 1

# Find the total votes to calculate candidate percenatages
total = sum(votes.values())

# Construct a candidates/votes nested list so the results can be sorted
results = sorted([[v, k] for k, v in votes.items()], reverse=True)

# Format the sorted (in reverse order) list for the report
lines = [f"{k + ':':12}{v:12,}{v/total * 100:11,.1f}%\n" for v, k in results]

# Generate the report string text
report = f"\
{' Election Results ':^36}\n\
{'--':-^36}\n\
{'Total Votes:':12}{total:12,}{100:11,.1f}%\n\
{'--':-^36}\n\
{''.join(lines)}\
{'--':-^36}\n\
{'Winner:':12}{results[0][0]:12,}{results[0][1]:>12}\n\
{'--':-^36}\n"

print(f"\n\n\n\n{report}\n\n\n\n")
