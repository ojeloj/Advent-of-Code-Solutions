from pathlib import Path 

# read puzzle input from file in local directory 
dir = Path(__file__).parent
with open(dir / 'puzzle-input.txt') as f:
    puzzle_input = f.read()

# make a sled class with three attributes, x and y-position and position history 
class Sled:
    def __init__(self, xPos, yPos, posHis):

        self.xPos = xPos
        self.yPos = yPos
        self.posHis = posHis

    # move sled 
    def move(self, dir):

        if dir == '<':
            self.xPos -= 1
        elif dir == '>':
            self.xPos += 1
        elif dir == 'v':
            self.yPos -= 1        
        elif dir == '^':
            self.yPos += 1

    # add position to position history
    def add_pos(self):
        self.posHis.append((self.xPos, self.yPos))

# make a sled object with initial x and y-positions at origin
sled = Sled(0, 0, [])

# add initial position to position history 
sled.add_pos()

for dir in puzzle_input:

    # move in directin given by drunk elf 
    sled.move(dir)

    # check if current position is in position history 
    if (sled.xPos, sled.yPos) not in sled.posHis:

        # add current position to history if not 
        sled.add_pos()

print(str(len(sled.posHis)) + ' houses recived at least one present.')