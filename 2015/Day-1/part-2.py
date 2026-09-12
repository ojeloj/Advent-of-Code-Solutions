# ask for puzzle input 
print('Puzzle input: ')
puzzle_input = str(input())

# floor variable 
floor = 0

# character position 
char_pos = 0

# loop through puzzle input 
for l in puzzle_input:

    if l == '(':
        floor += 1
    else:
        floor -= 1
    
    char_pos += 1
    
    if floor == -1:
        print('The position of the character is: ' + str(char_pos))
        break 
