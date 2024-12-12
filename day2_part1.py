reports = []

# with open("day2_input_sample.txt", "r") as file:
with open("day2_input.txt", "r") as file:
    for line in file:
        differences = []
        line = line.strip()
        report = line.split(" ")
        reports.append(report)

num_safe = 0

for report in reports:    
    differences = []
    safe = True 

    for index in range(len(report)):

        next = index + 1
        if next >= len(report):
            break

        diff = int(report[next]) - int(report[index])
        if abs(diff) > 3:
            safe = False 
            break

        differences.append(diff)

    if safe: 
        all_positive = all(value > 0 for value in differences)
        all_negative = all(value < 0 for value in differences)

        if all_positive or all_negative: 
            num_safe += 1

print(num_safe)
