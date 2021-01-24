## 2048 Game
import pygame
pygame.init()
from MatrixManipulation import *
from pygame.locals import *


# Matrix full of 0s
matrix = []
for i in range(4):
    matrix.append ([])
    for j in range(4):
        matrix[i].append(0)
        
addNum(matrix)
addNum(matrix)

print_matrix(matrix)

playing = 1

while playing == 1:

    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_UP:
                matrix = swipeUp(matrix)
            if event.key == K_RIGHT:
                matrix = swipeRight(matrix)
            if event.key == K_LEFT:
                matrix = swipeLeft(matrix)
            if event.key == K_DOWN:
                matrix = swipeDown(matrix)
            print_matrix(matrix)

    for i in range (0, 4):
        for j in range (0, 4):
            if matrix[i][j] == 2048:
                print("Congratulations! You've won!")
                playing = 0
    

