list_one = []
list_two = []

with open("day1_input.txt", 'r') as file: 
    for line in file: 
        line = line.strip() 
        pieces = line.split("   ")
        list_one.append(int(pieces[0]))
        list_two.append(int(pieces[1]))

score = 0 

for value1 in list_one: 
    num_appearances = 0 
    for value2 in list_two: 
        if value1 == value2: 
            num_appearances += 1 
    score += value1 * num_appearances

print(score)