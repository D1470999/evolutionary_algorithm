"""
#grid simulation
grd_size = 10

grid = []
for - in range(grid_size):
    grid.append(['.']*grid_size)

def print_grid(grid):
    for row in grid:
        for char in row:
            print(char, end = ' ') #prints just the characters and puts a space at the end
        print()

print_grid(grid) = square grid of periods
_________________
"""
import random
import time
import os

#every cell either contains a wanderer or is empty
class Plant:
    def __init__(self, r, c):
        self.r = r
        self.c = c
    def __str__(self):
        return '.'
    def next_pos(self):
        return (self.r, self.c) #returning next position (the same, because plants can't move), in case, if you want to know in the future... consistency

#the wanderer shows where it wants to move to, doesn't actually move, the world moves it
class Wanderer:
    def __init__(self, r, c):
        self.r = r
        self.c = c
    def __str__(self):
        return 'W'
    def next_pos(self):
        rdiff = [-1, -1, -1, 0, 0, 1, 1, 1]
        cdiff = [-1, 0, 1, -1, 1, -1, 0, 1]
        n = rand_num = random.randint(0, 7)
        return (self.r + rdiff[n], self.c + cdiff[n])  #random pairing, returning new position

class World:
    def __init__(self, grid_size):
        self.grid_size = grid_size
        self.grid = []
        for _ in range(grid_size):
            self.grid.append([' '] * grid_size)
        for r in range(grid_size):
            for c in range(grid_size):
                self.grid[r][c] = Plant(r, c)
        self.wanderer = Wanderer(5, 5) #keeping track of wanderer, variable directly refering to position
        self.grid[5][5] = self.wanderer

    def __str__(self):
        output = ""
        for row in self.grid:
            for char in row:
                output += str(char) + ' '
            output += "\n"
        return output

    #only keeping track of one person so this is easier, will have to loop through everything once u have multiple ppl, sending wanderer where it wants to go
    def next(self):
        new_r, new_c = self.wanderer.next_pos()
        if 0 <= new_r < self.grid_size and 0 <= new_c < self.grid_size: #making it an arena.... since what happens if he wants to leave the world
            r, c = self.wanderer.r, self.wanderer.c
            self.grid[r][c] = Plant(r, c)
            self.grid[new_r][new_c] = self.wanderer
            self.wanderer.r = r
            self.wanderer.c = c

world = World(10) #gives parameters needed to call it
print(world)
while True:
    os.system('clear')
    print(world)
    world.next()
    time.sleep(1)
