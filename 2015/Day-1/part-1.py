from pathlib import Path 

# read puzzle input from file in local directory 
dir = Path(__file__).parent
with open(dir / 'puzzle-input.txt') as f:
    puzzle_input = f.read()

# floor variable 
floor = 0

# loop through puzzle input 
for l in puzzle_input:

    if l == '(':
        floor += 1
    else:
        floor -= 1

print('Santa is on floor: ' + str(floor))