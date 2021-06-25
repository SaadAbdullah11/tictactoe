# -*- coding: utf-8 -*-
"""
Created on Thu Jun 24 16:29:48 2021

@author: Saad
"""

import pygame, sys
import numpy as np
pygame.init()
    
WIDTH=600
HEIGHT=600

RED=(255,0,0)
BG_COLOR=(20,200,35)

LINE_WIDTH=15
LINE_COLOR=(23,145,135)

BOARD_ROWS=3
BOARD_COLS=3

CIRCLE_RADIUS=60
CIRCLE_WIDTH=15

screen=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('TIC TAC TOE')
screen.fill(BG_COLOR)

#board
board=np.zeros((BOARD_ROWS, BOARD_COLS))

#pygame.draw.line( screen,RED,(10,10),(300,300),10 )

def draw_lines():
    #1st horizontal
    pygame.draw.line(screen, LINE_COLOR, (0,200), (600,200) , LINE_WIDTH)
    #2nd horizontal
    pygame.draw.line(screen, LINE_COLOR, (0,400), (600,400) , LINE_WIDTH)
    #1st vertical
    pygame.draw.line(screen, LINE_COLOR, (200,0), (200,600) , LINE_WIDTH)
    #2nd vertical
    pygame.draw.line(screen, LINE_COLOR, (400,0), (400,600) , LINE_WIDTH)

def draw_figures():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col]==1:
                pygame.draw.circle(screen,RED,(int(col* 200+100),int(row*200+100)),CIRCLE_RADIUS, CIRCLE_WIDTH)
def mark_square(row,col,player):
    board[row][col] = player

def available_square(row,col):
        return board [row][col]==0

def is_board_full():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col]==0:
                return False
    return True

print(is_board_full())
# marking all the squares
for row in range(BOARD_ROWS):
    for col in range(BOARD_COLS):
        mark_square(row,col,1)
# row is full -True
print(is_board_full())

print(board)
draw_lines()
player=1
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()
        if event.type==pygame.MOUSEBUTTONDOWN:
            
            mouseX=event.pos(0) #x
            mouseY=event.pos(1) #y
            clicked_row=int(mouseY // 200)
            clicked_col=int(mouseX // 200)
            print(clicked_row)
            print(clicked_col)
            if available_square(clicked_row,clicked_col):
                if player==1:
                    mark_square(clicked_row,clicked_col,1)
                    player=2
                elif player==2:
                    mark_square(clicked_row,clicked_col,2)
                    player=1
                    print(board)
                  
    pygame.display.update()
print(board)