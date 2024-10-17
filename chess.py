import os
import numpy as np
import pygame as pygame
from enum import Enum

import chess_board

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

colors = [(255,0,0),(255, 94, 0),(251, 255, 0),(0,255,0),(0,0,255),(255, 0, 255)]

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
            
            
            pygame.draw.rect(screen, color = white if draw_white else black, rect=rect)
            
            if board[y][x] != 0:
                pygame.draw.circle(screen, color=pygame.Color(colors[abs(board[y][x])-1]), center=(x_pos + rect_size/2,y_pos + rect_size/2), radius=10)
            draw_white = not draw_white

        draw_white = not draw_white


screen = pygame.display.set_mode((screen_size,screen_size))
pygame.init()

gameboard = chess_board.GameBoard()

running = True

from_pos = np.empty(0)
to_pos = np.empty(0)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_focused():
                mouse_pos = np.array(pygame.mouse.get_pos())/rect_size + (-0.5,0)
                game_pos = mouse_pos.astype(int)[::-1]
                if from_pos.size == 0:
                    from_pos = game_pos
                elif to_pos.size == 0:
                    to_pos = game_pos
                    if (from_pos.size != 0 and to_pos.size != 0):
                        try:
                            gameboard.move_to(from_pos,to_pos)
                        except:
                            print("move error -> reset")
        
                    from_pos = np.empty(0)
                    to_pos = np.empty(0)

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")
    
    drawBoard(gameboard.board, side_size)
    
    # flip() the display to put your work on screen
    pygame.display.flip()

pygame.quit()