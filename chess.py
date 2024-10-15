import os
import numpy as np
import pygame as pygame
from enum import Enum

screen_size = 700
side_size = 8
margin = 20

draw_screen_size = screen_size - margin * 4
rect_size = draw_screen_size/side_size


white = (173, 167, 149)
black = (36, 31, 26)

class PieceType(Enum):
    Pawn = 1, 
    Castle = 2,
    Knight = 3,
    Bishop = 4,
    Queen = 5,
    King = 6


#valid_castle = lambda x: True if (x[0] != 0 and x[1] > 0) or (x[1] != 0 and x[0] > 0) else False
#valid_pawn   = lambda x: True if (x[0]  > 0 and x[1] == 0) else False

def valid_castle(cur_pos, new_pos):
    if cur_pos[0] != new_pos[0] and cur_pos[1] != new_pos[1]:
         return False
    
piece_move_check = {

    6: valid_castle
}

class Tile:
    def __init__(this,x,y, color, piece_type =0):
        this.x = x
        this.y = y
        this.piece_type = piece_type
        this.color = color
    
    def is_occupied(this):
        return True if this.piece_type > 0 else False
    
    def set_piece(this, piece_type):
        if this.is_occupied == True: return
        this.piece_type = piece_type
        return True
    
    def replace_piece(this, new_piece):
        pass
        
    def draw(this):
        pass

class GameBoard:
    def __init__(this):
        this.board = np.array([[(0,"empty") for _ in range(side_size)] for _ in range (side_size)])
        this.board[1] += 1
        this.board[-2] += 1
        this.board[0] += [2,3,4,6,5,4,3,2]
        this.board[-1] += [2,3,4,5,6,4,3,2]
    
    def piece_at(this, x, y):
        pass


def valid_pawn(tile, new_pos):

    pass

def drawBoard(board, size):
    draw_white = True
    tile_list = []
    for x in range(board.shape[0]):
        for y in range(board.shape[1]):
            x_pos = margin*2 + rect_size * x
            y_pos = margin   + rect_size * y

            rect = pygame.Rect(x_pos, y_pos ,rect_size,rect_size)
            fill = white if draw_white else black

            
            tile_list.append(Tile(x_pos, y_pos,
                                  'white' if draw_white else 'black',
                                  board[y][x]))
            
            

            if board[y][x] == 2:
                pygame.draw.circle(screen, color=pygame.Color(255,0,0), center=(x_pos + rect_size/2,y_pos + rect_size/2), radius=10)
            
            draw_white = not draw_white

        draw_white = not draw_white


screen = pygame.display.set_mode((screen_size,screen_size))
pygame.init()

running = False

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_focused():
                mouse_pos = pygame.mouse.get_pos()
                print(mouse_pos)

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")

    # RENDER YOUR GAME HERE
    
    drawBoard(side_size)
    # flip() the display to put your work on screen
    pygame.display.flip()

pygame.quit()