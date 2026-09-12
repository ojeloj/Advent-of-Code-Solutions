# ask for puzzle input 
print('Puzzle input: ')
puzzle_input = str(input())

# floor variable 
floor = 0

# loop through puzzle input 
for l in puzzle_input:

    if l == '(':
        floor += 1
    else:
        floor -= 1

print('Santa is on floor: ' + str(floor))