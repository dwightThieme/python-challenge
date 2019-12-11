with open(input_path, newline='') as csvfile:
    csv_obj = csv.reader(csvfile, delimiter=',')
    csv_list = list(csv_obj)

print(f"  csv_read:\n\n         {csv_obj}\n\n")

print("  csv_list head:\n\n  [")
for record in range(10):
    print("       ", csv_list[record])

print("  ]\n\n\n\n")