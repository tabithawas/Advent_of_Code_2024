list_one = []
list_two = []

with open("day1_input.txt", 'r') as file: 
    for line in file: 
        line = line.strip() 
        pieces = line.split("   ")
        list_one.append(int(pieces[0]))
        list_two.append(int(pieces[1]))

list_one.sort() 
list_two.sort() 

sum = 0; 

for index, value in enumerate(list_one): 
    difference = value - list_two[index]
    sum += abs(difference)

print(sum)