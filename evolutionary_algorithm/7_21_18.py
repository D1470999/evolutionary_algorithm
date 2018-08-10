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
        self.energy -= 1
        return self.energy
    def reproduce(self):
        self.energy -= 10
    def find_food(self):
        new_r = [-1, -1, -1, 0, 0, 1, 1, 1]
        new_c = [-1, 0, 1, -1, 1, -1, 0, 1]
        for i in range(8):
            check_r = self.r - new_r[i]
            check_c = self.c - new_c[i]
            if 0 <= check_r < world.grid_size and 0 <= check_c < world.grid_size:
                if world.grid[check_r][check_c] == Plant(check_r, check_c):
                    return check_r, check_c

                else:
                    return 'X'

    def next_pos(self):
        if self.find_food() != 'X':
            return self.find_food()
        else:
            rdiff = [-1, -1, -1, 0, 0, 1, 1, 1]
            cdiff = [-1, 0, 1, -1, 1, -1, 0, 1]
            n = rand_num = random.randint(0, 7)
            new_r, new_c = self.r + rdiff[n], self.c + cdiff[n]
            return new_r, new_c

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
        return 'C'
    def eat(self):
        self.energy += 2
        return self.energy

class Bear(Animal):
    def __init__(self, r, c):
        self.r = r
        self.c = c
        self.age = 0
        self.energy = 5
    def __str__(self):
        return 'B'
    def eat(self):
        self.energy += 2
        return self.energy

class Human(Animal):
    def __init__(self, r, c):
        self.r = r
        self.c = c
        self.age = 0
        self.energy = 5
    def __str__(self):
        return 'H'
    def eat(self):
        self.energy += 2
        return self.energy

class World:
    def __init__(self, grid_size):
        self.grid_size = grid_size
        self.grid = []
        self.plants = []
        self.cows = []
        self.bears = []
        self.humans = []
        self.empty = []
        for _ in range(grid_size):
            self.grid.append([' '] * grid_size)
        for r in range(grid_size):
            for c in range(grid_size):
                self.grid[r][c] = Plant(r, c)
                self.plants.append((r, c))
        for i in range(50):
            self.cows.append(Cow(25, i))
            self.grid[25][i] = Cow(25, i)
        for i in range(0, 50, 2):
            self.cows.append(Bear(23, i))
            self.grid[23][i] = Bear(23, i)
        for i in range(0, 50, 5):
            self.humans.append(Human(30, i))
            self.grid[30][i] = Human(30, i)
        self.new_grid = deepcopy(self.grid)
    def __str__(self):
        output = ""
        for row in self.grid:
            for char in row:
                output += str(char) + ' '
            output += "\n"
        return output

    def next(self):
        for cow in self.cows:
            new_r, new_c = cow.next_pos()
            cow.energy = cow.health()
            age = cow.growth()
            r, c = cow.r, cow.c
            if cow.energy <= 0:
                self.new_grid[r][c] = Empty(r,c)
                self.empty.append((r, c))
                self.cows.remove(cow)
                continue
            elif age >= 100:
                self.new_grid[r][c] = Empty(r,c)
                self.empty.append((r, c))
                self.cows.remove(cow)
                continue
            if 0 <= new_r < self.grid_size and 0 <= new_c < self.grid_size and self.new_grid[new_r][new_c] == Cow(new_r, new_c):
                while self.new_grid[new_r][new_c] == Cow(new_r, new_c):
                    new_r, new_c = cow.next_pos()
            if 0 <= new_r < self.grid_size and 0 <= new_c < self.grid_size:
                self.new_grid[new_r][new_c] = cow
                self.new_grid[r][c] = Empty(r, c)
                self.empty.append((r, c))
                if (new_r, new_c) in self.plants:
                    cow.energy = cow.eat()
                    self.plants.remove((new_r, new_c))
                elif (new_r, new_c) in self.empty:
                    self.empty.remove((new_r, new_c))
                cow.r = new_r
                cow.c = new_c
            if cow.energy > 20:
                cow.reproduce()
                if 0<= cow.c +1 < self.grid_size:
                    self.cows.append(Cow(cow.r, cow.c+1))
                else:
                    self.cows.append(Cow(cow.r, cow.c-1))

        for bear in self.bears:
            new_r, new_c = bear.next_pos()
            bear.energy = bear.health()
            age = bear.growth()
            r, c = bear.r, bear.c
            if bear.energy <= 0:
                self.new_grid[r][c] = Empty(r,c)
                self.bears.remove(bear)
                self.empty.append((r, c))
                continue
            elif age >= 100:
                self.new_grid[r][c] = Empty(r,c)
                self.bears.remove(bear)
                self.empty.append((r, c))
                continue
            if 0 <= new_r < self.grid_size and 0 <= new_c < self.grid_size and self.new_grid[new_r][new_c] == Bear(new_r, new_c):
                while self.new_grid[new_r][new_c] == Bear(new_r, new_c):
                    new_r, new_c = bear.next_pos()
            if 0 <= new_r < self.grid_size and 0 <= new_c < self.grid_size:
                self.new_grid[new_r][new_c] = bear
                self.new_grid[r][c] = Empty(r, c)
                self.empty.append((r, c))
                if (new_r, new_c) in self.cows:
                    bear.energy = bear.eat()
                    self.plants.remove((new_r, new_c))
                elif (new_r, new_c) in self.empty:
                    self.empty.remove((new_r, new_c))
                bear.r = new_r
                bear.c = new_c
            if bear.energy > 20:
                bear.reproduce()
                if 0<= bear.c +1 < self.grid_size:
                    self.bears.append(Bear(bear.r, bear.c+1))
                else:
                    self.bears.append(Bear(bear.r, bear.c-1))
        for human in self.humans:
            new_r, new_c = human.next_pos()
            human.energy = human.health()
            age = human.growth()
            r, c = human.r, human.c
            if human.energy <= 0:
                self.new_grid[r][c] = Empty(r,c)
                self.humans.remove(human)
                self.empty.append((r, c))
                continue
            elif age >= 100:
                self.new_grid[r][c] = Empty(r,c)
                self.humans.remove(human)
                self.empty.append((r, c))
                continue
            if 0 <= new_r < self.grid_size and 0 <= new_c < self.grid_size and self.new_grid[new_r][new_c] == Human(new_r, new_c):
                while self.new_grid[new_r][new_c] == Human(new_r, new_c):
                    new_r, new_c = human.next_pos()
            if 0 <= new_r < self.grid_size and 0 <= new_c < self.grid_size:
                self.new_grid[new_r][new_c] = human
                self.new_grid[r][c] = Empty(r, c)
                self.empty.append((r, c))
                if (new_r, new_c) in self.cows:
                    human.energy = human.eat()
                    self.cows.remove((new_r, new_c))
                elif (new_r, new_c) in self.empty:
                    self.empty.remove((new_r, new_c))
                if (new_r, new_c) in self.plants:
                    human.energy = human.eat()
                    self.plants.remove((new_r, new_c))
                elif (new_r, new_c) in self.empty:
                    self.empty.remove((new_r, new_c))
                human.r = new_r
                human.c = new_c
            if human.energy > 20:
                human.reproduce()
                if 0<= human.c +1 < self.grid_size:
                    self.humans.append(Human(human.r, human.c+1))
                else:
                    self.human.append(Human(human.r, human.c-1))
        a = rand_num = random.randint(0, len(self.empty))
        new_x, new_y = self.empty[a]
        if 0 <= new_x < self.grid_size and 0 <= new_y < self.grid_size and (new_x, new_y) not in self.cows and (new_x, new_y) not in self.bears and (new_x, new_y) not in self.cows:
            self.plants.append((new_x, new_y))
            self.empty.remove((new_x, new_y))
            self.new_grid[new_x][new_y] = Plant(new_x, new_y)


        self.grid = deepcopy(self.new_grid)






world = World(50) #gives parameters needed to call it
cow = Cow(5, 5)
print(world)
generation = 1
while generation > 0:
    os.system('clear')
    print(world)
    print("Generation " + str(generation))
    #for cow in world.cows:
        #r, c = cow.next_pos()
    #    print(world.new_grid[cow.next_r][cow.next_c] == cow)
        #print(cow.energy, world.test)
    #print(world.babies)
    print(len(world.cows))
    generation += 1
    world.next()
    time.sleep(.3)
