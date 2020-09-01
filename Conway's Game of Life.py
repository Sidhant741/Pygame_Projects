# Conwoy's Game of Life
"""
It is a cellular automaton. It is a zero-player game, meaning that its evolution is determined by its initial state,
requiring no further input. One interacts with this by creating an initial configuration and observing how it evolves.
Rules:
Any live cell with fewer than two live neighbours dies, as if by underpopulation.
Any live cell with two or three live neighbours lives on to the next generation.
Any live cell with more than three live neighbours dies, as if by overpopulation.
Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.
"""

# Importing the Libraries
import pygame
import numpy as np
np.set_printoptions(threshold=np.inf)

# Global variables
pygame.init()
window_width = 500
window_height = 500
white = (255, 255, 255)
black = (0, 0, 0)


# Game
class Game:
    def __init__(self):
        self.fps = 5
        self.clock = pygame.time.Clock()
        self.cells = self.adding_points_at_start()
        self.window = pygame.display.set_mode((window_width, window_height))
        self.gameloop()

    def gameloop(self):
        run = True
        while run:
            self.window.fill(black)
            self.draw()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
            self.update()
            self.clock.tick(self.fps)
            pygame.display.update()

    def draw(self):
        for i in self.cells:
            pygame.draw.rect(self.window, white, (i[1]*10, i[0]*10, 10, 10))

    def adding_points_at_start(self):
        cells_coordinates = []
        temp = int(input('Do u want to add points(press 1) or add single Patterns(press 2)'))
        if temp == 2:
            return self.images()
        else:
            print('The values that x and y can take are in between 0 and 49 (both inclusive) with a width of 10')

            while True:
                row = int(input('Enter the row no'))
                column = int(input('Enter the column no'))
                cells_coordinates.append((row, column))
                if input('Press y if u want to add more points').lower() == 'y':
                    continue
                else:
                    break

            print('These are the points with living cells', cells_coordinates)
            return cells_coordinates

    def update(self):
        neighbors = np.zeros((50, 50), dtype=int)
        for row in range(50):
            for column in range(50):
                temp = self.count_neighbors(row, column)
                neighbors[row][column] = temp
        self.cells = self.next_gen(neighbors)

    def count_neighbors(self, x, y):
        neighbors = 0
        temp = self.cells.copy()
        try:
            temp.remove((x, y))
        except:
            pass
        for j, k in temp:
            if abs(j - x) == 1 and abs(k - y) == 0:  # for checking left and right
                neighbors += 1
                print('for checking left and right')
            elif abs(j - x) == 0 and abs(k - y) == 1:  # for checking top and bottom
                neighbors += 1
                print('for checking top and bottom')
            elif abs(j - x) == 1 and abs(k - y) == 1:  # for diagonals
                neighbors += 1
                print('for diagonals')
        return neighbors

    def next_gen(self, neighbors):
        future_cells = set()
        for i in range(50):
            for j in range(50):
                if neighbors[i][j] == 3 and (i, j) not in self.cells:
                    future_cells.add((i, j))
                    print(i, j, 1)
                elif neighbors[i][j] == 3 and (i, j) in self.cells:
                    future_cells.add((i, j))
                    print(i, j, 2)
                elif neighbors[i][j] == 2 and (i, j) in self.cells:
                    future_cells.add((i, j))
                    print(i, j, 3)
        return future_cells

    def images(self):
        print('Press 1 for Block')
        print('Press 2 for a Glider')
        print('Press 3 for a Blinker')
        print('Press 4 for a Bee Hive')
        print('Press 5 for a Toad')
        print('Press 6 for a Lightweight Spaceship')
        print('Press 7 for a Gosper glider gun')
        temp = int(input())
        if temp == 1:
            cells = [(1, 2), (1, 3), (2, 2), (2, 3)]
            return cells
        elif temp == 2:
            cells = [(3, 4), (4, 5), (5, 3), (5, 4), (5, 5)]
            return cells
        elif temp == 3:
            cells = [(1, 2), (2, 2), (2, 3)]
            return cells
        elif temp == 4:
            cells = [(3, 3), (2, 4), (2, 5), (3, 6), (4, 5), (4, 4)]
            return cells
        elif temp == 5:
            cells = [(4, 4), (4, 5), (4, 6), (3, 5), (3, 6), (3, 7)]
            return cells
        elif temp == 6:
            cells = [(11, 2), (11, 3), (12, 1), (12, 2), (12, 3), (12, 4), (13, 1), (13, 2), (13, 4), (13, 5), (14, 3), (14, 4)]
            return cells
        elif temp == 7:
            lb= [(23, 9), (23, 8), (24, 9), (24, 8)]
            rb = [(22, 42), (22, 43), (23, 42), (23, 43)]
            lm = [(21, 20), (21, 21), (22, 19), (22, 23), (23, 18), (24, 18), (25, 18), (26, 19), (27, 20), (27, 21), (26, 23),
                  (25, 24), (24, 24), (23, 24), (24, 25), (24, 22)]
            rm = [(24, 30), (24, 32), (25, 32), (23, 29), (23, 28), (22, 29), (22, 28), (21, 29), (21, 28), (20, 30), (20, 32), (19, 32)]
            cells = lb+rb+lm+rm
            return cells


game = Game()
