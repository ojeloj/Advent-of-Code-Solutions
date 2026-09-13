from pathlib import Path 
import math 

# read puzzle input from file in local directory 
dir = Path(__file__).parent
with open(dir / 'puzzle-input.txt') as f:
    puzzle_input = f.read().splitlines()

# process puzzle input so that we end up with a list of present dimensions
data = []
for l in puzzle_input:
    data.append(list(map(int, l.split('x'))))

# function that computes the total amount of ribbon needed 
# for a single present
def sing_pres_rib(present_size):

    # sort in ascending order
    present_size.sort()
    
    return 2*present_size[0] + 2*present_size[1] + math.prod(present_size)

# Compute total amount of ribbon needed
total_rib = sum([sing_pres_rib(x) for x in data])
print('The elves will need ' + str(total_rib) + ' feet of ribbon.')