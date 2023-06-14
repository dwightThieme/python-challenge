import csv
import os

csv_path = os.path.join(os.path.dirname(__file__), "Resources", "election_data.csv")

# with open(csv_path, encoding="utf-8", newline="") as csvfile:
#     csv_read = csv.reader(csvfile)

#     next(csv_read)

#     votes = {}

#     for row in csv_read:
#         votes[row[2]] = votes.get(row[2], 0) + 1

# print("\n" + 32 * "-")
# for k in sorted(votes, key=votes.get, reverse=True):
#     print(f"{k:24} {votes[k]:7,}")
# print("-" * 32 + "\n")
# sep = "-"*32
# print(f"\n{'-'*32}")
# print("\n"+sep)

# ---------------------------------------------------------------------------- #

# import os
# import csv
# from collections import Counter

# election_data_csv = os.path.join("Resources", "election_data.csv")

# with open(election_data_csv, "r") as file:
#     votes = dict(Counter(([row[2] for row in list(csv.reader(file))[1:]]))

# winner = max(votes.items(), key=lambda col: col[1])
# voted = sum(votes.values())

# for k, v in sorted(votes.items()):
#     print(f"{k:25} {v:10,} {v/voted:10.2%}")

# ---------------------------------------------------------------------------- #

# with open(csv_path, encoding="utf-8", newline="") as csvfile:
#     votes = [row[2] for row in list(csv.reader(csvfile))][1:]

# results = {name: votes.count(name) for name in sorted(set(votes))}
# most = max(results.items(), key=lambda r: r[1])

# for k, v in results.items():
#     print(f"{k:24}{v:8,}")

# print(f"\n{most[0]:24}{most[1]:8,}")

# ---------------------------------------------------------------------------- #

# with open(csv_path, encoding="utf-8") as csvfile:
#     csv_reader = csv.reader(csvfile, delimiter=",")

#     next(csv_reader)

#     candidates = []
#     votes = []
#     totals = []

#     for row in csv_reader:
#         votes.append(row[2])
#         if row[2] not in candidates:
#             candidates.append(row[2])
#             totals.append(0)

# print(candidates)
# print(totals)

# for i in range(len(votes)):
#     for j in range(len(candidates)):
#     if candidates[j] == votes[i]:
#             totals[j] += 1

# print(candidates)
# print(totals)

# ---------------------------------------------------------------------------- #

# import os
# import csv
# from collections import Counter

# election_data_csv = os.path.join("Resources", "election_data.csv")

# with open(election_data_csv, "r") as file:
#     votes = dict(Counter(([row[2] for row in list(csv.reader(file))[1:]]))

# winner = max(votes.items(), key=lambda col: col[1])
# voted = sum(votes.values())

# for k, v in sorted(votes.items()):
#     print(f"{k:25} {v:10,} {v/voted:10.2%}")

# ---------------------------------------------------------------------------- #

# election_data_csv = os.path.join("Resources", "election_data.csv")

# with open(election_data_csv, "r") as file:
#     rows = list(csv.reader(file))

# votes = dict(Counter((row[2] for row in rows[1:])))

# winner, most = max(votes.items(), key=lambda col: col[1])
# voted = sum(votes.values())

# print(f"\n\n{winner:25} {most:10,} {most/voted:10.2%}\n\n")

# for k, v in sorted(votes.items()):
#     print(f"{k:25} {v:10,} {v/voted:10.2%}")


# ---------------------------------------------------------------------------- #
