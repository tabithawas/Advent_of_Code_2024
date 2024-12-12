reports = []

# with open("day2_input_sample.txt", "r") as file:
with open("day2_input.txt", "r") as file:
    for line in file:
        line = line.strip()
        temp_report = line.split(" ")
        report = []
        for item in temp_report: 
            report.append(int(item))
        reports.append(report)

def check_if_safe(report) -> bool:

    differences = []

    for index in range(len(report)):

        next = index + 1
        if next >= len(report):
            break

        diff = report[next] - report[index]
        if abs(diff) > 3:
            return False 

        differences.append(diff)

    all_positive = all(value > 0 for value in differences)
    all_negative = all(value < 0 for value in differences)

    if all_positive or all_negative: 
        return True 
    
    return False 

def generate_alt_reports(report) -> list: 
    new_reports = [] 

    for index in range(len(report)): 
        new_report = report[:]
        del new_report[index]
        new_reports.append(new_report)
    
    return new_reports

num_safe = 0

for report in reports: 
    safe = check_if_safe(report)
    if safe: 
        num_safe += 1
    else: 
        alt_reports = generate_alt_reports(report) 
        for alt_report in alt_reports: 
            alt_safe = check_if_safe(alt_report)
            if alt_safe: 
                num_safe += 1
                break

print(num_safe)