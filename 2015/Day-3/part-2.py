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
sled_santa = Sled(0, 0, [])
sled_robo = Sled(0, 0, [])

# add initial position to position history 
sled_santa.add_pos()
sled_robo.add_pos()

for index in range(0, len(puzzle_input)):

    # move in directin given by drunk elf 
    if index % 2 == 0:
        sled_robo.move(puzzle_input[index])

        # check if current position is in position history 
        if (sled_robo.xPos, sled_robo.yPos) not in sled_robo.posHis:

            # add current position to history if not 
            sled_robo.add_pos()

    else:
        sled_santa.move(puzzle_input[index])

        # check if current position is in position history 
        if (sled_santa.xPos, sled_santa.yPos) not in sled_santa.posHis:

            # add current position to history if not 
            sled_santa.add_pos()

print(str(len(set(sled_santa.posHis).union(sled_robo.posHis))) + ' houses recived at least one present.')