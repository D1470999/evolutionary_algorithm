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
create a list, full of wanderers...keep track of where they all are
BUT INSTEAD WE CAN:
for i in range
    for j in range
        if instance of(grid[i][j], wanderer)
now calculate next position, they all have to do something at the same time....solution: create a copy, adjust it in the copy of the grid,
if they want to land on the same square: 2nd guy has to choose somewhere else, or u have some way to determine who gets that square... health??
makes a list that keeps track of position

[wanderer(r, c), wanderer(r, c)]


#for i in range(len(self.wanderers)):
#    x = self.wanderers[i].r
#    y = self.wanderers
#    grid[x][y] = wanderer[i]
#check the original grid according to original data
#check if there is wanderer,
#check its next position
#check if two wanderers want to go to the same place-if so, the one with bigger age takes that spot and the other moves to another place
#put its next position in the new grid
#change the wanderers into the wanderer next position
        for wanderer in self.wanderers:
            r = wanderer.r
            c = wanderer.c
            self.grid[r][c] = wanderer
        for i in range(len(self.wanderers)):
            x = self.wanderers[i].r
            y = self.wanderers[i].c
            self.grid[x][y] = self.wanderers[i]
    def wanderers_list():
        return self.wanderers
_________________
"""
import random
import time
import os
from copy import deepcopy

class Empty:
    def __init__(self, r, c):
        self.r = r
        self.c = c
    def __str__(self):
        return '.'
    def next_pos(self):
        return (self.r, self.c)

class Animal:
    def __init__(self):
        self.age = 0
        self.energy = 5
    def growth(self):
        self.age += 1
        return self.age
    def health(self):
        self.energy -= self.age
        return self.energy
    def eat(self):
        self.energy += 1
        return self.energy
    def reproduce(self):
        self.energy -= 10

class Plant:
    def __init__(self, r, c):
        self.r = r
        self.c = c
    def __str__(self):
        return '%'
    def next_pos(self):
        return (self.r, self.c)
    def new_plant(self):
        rdiff = [-1, -1, -1, 0, 0, 1, 1, 1]
        cdiff = [-1, 0, 1, -1, 1, -1, 0, 1]
        n = rand_num = random.randint(0, 7)
        return (self.r + rdiff[n], self.c + cdiff[n])

class Cow(Animal):
    def __init__(self, r, c):
        self.r = r
        self.c = c
        self.age = 0
        self.energy = 5
    def __str__(self):
        return 'W'
    def next_pos(self):
        rdiff = [-1, -1, -1, 0, 0, 1, 1, 1]
        cdiff = [-1, 0, 1, -1, 1, -1, 0, 1]
        n = rand_num = random.randint(0, 7)
        return (self.r + rdiff[n], self.c + cdiff[n])

class Bear(Animal):
    def __init__(self, r, c):
        self.r = r
        self.c = c

class Human(Animal):
    def __init__(self, r, c):
        self.r = r
        self.c = c

class World:
    def __init__(self, grid_size):
        self.grid_size = grid_size
        self.grid = []
        self.cows = []
        self.plant = Plant(25, 25)
        self.age = 45
        for _ in range(grid_size):
            self.grid.append([' '] * grid_size)
        for r in range(grid_size):
            for c in range(grid_size):
                self.grid[r][c] = Plant(r, c)
        for i in range(50):
            self.cows.append(Cow(25, i))
            self.grid[25][i] = Cow(25, i)
    def __str__(self):
        output = ""
        for row in self.grid:
            for char in row:
                output += str(char) + ' '
            output += "\n"
        self.new_grid = deepcopy(self.grid)
        return output

    def next(self):
        for cow in self.cows:
            new_r, new_c = cow.next_pos()
            new_x, new_y = self.plant.new_plant()
            health = cow.health()
            age = cow.growth()
            r, c = cow.r, cow.c
            if cow.energy < 0:
                self.new_grid[r][c] = Empty(r,c)
            elif age >= 100:
                self.new_grid[r][c] = Empty(r,c)
            if 0 <= new_r < self.grid_size and 0 <= new_c < self.grid_size:
                self.new_grid[new_r][new_c] = cow
                self.new_grid[r][c] = Empty(r, c)
                cow.r = new_r
                cow.c = new_c
                if new_r == new_x and new_c == new_y:
                    cow.energy = cow.eat()
            if cow.energy > 15:
                cow.reproduce()
                self.cows.append(Cows(cow.r, cow.c+1))
        if 0 <= new_x < self.grid_size and 0 <= new_y < self.grid_size and new_r != new_x and new_c != new_y:
            r, c = self.plant.r, self.plant.c
            self.new_grid[new_x][new_y] = self.plant
            self.plant.r = new_x
            self.plant.c = new_y
        self.grid = self.new_grid[:]
        self.new_grid = deepcopy(self.grid)





world = World(50) #gives parameters needed to call it
cow = Cow(5, 5)
print(world)
generation = 1
while generation > 0:
    os.system('clear')
    print(world)
    print("Generation " + str(generation))
    for cow in world.cows:
        print(cow.age, cow.energy)
    generation += 1
    world.next()
    time.sleep(.2)
