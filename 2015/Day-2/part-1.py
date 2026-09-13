from pathlib import Path 

# read puzzle input from file in local directory 
dir = Path(__file__).parent
with open(dir / 'puzzle-input.txt') as f:
    puzzle_input = f.read().splitlines()

# process puzzle input so that we end up with a list of present dimensions
data = []
for l in puzzle_input:
    data.append(list(map(int, l.split('x'))))

# function that computes the total amount of paper needed 
# for a single present
def sing_pres_paper(present_size):

    w = present_size[0]
    h = present_size[1]
    l = present_size[2]

    return 2*l*w + 2*w*h + 2*h*l + min(l*w, w*h, h*l)

# Compute total amount of paper needed
total_paper = sum([sing_pres_paper(x) for x in data])
print('The elves will need ' + str(total_paper) + ' square feet of paper.')