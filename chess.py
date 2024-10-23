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

colors_light = [(255,0,0),(255, 94, 0),(251, 255, 0),(0,255,0),(0,0,255),(255, 0, 255)]
colors_dark = [(110, 15, 0),(140, 46, 6),(153, 104, 24),(55, 74, 7),(0, 17, 99),(119, 0, 128)]

pieces = ["Empty","Pawn","Castle","Horse","Bishop","Queen","King"]


def drawBoard(board, size):
    draw_white = True
    tile_list = []
    for x in range(board.shape[0]):
        for y in range(board.shape[1]):
            x_pos = margin * 2 + rect_size * x
            y_pos = margin * 2  + rect_size * y

            rect = pygame.Rect(x_pos, y_pos ,rect_size,rect_size)
            pygame.draw.rect(screen, color = white if draw_white else black, rect=rect)
            
            if board[y][x] != 0:
                if board[y][x] > 0:
                    text_color = colors_dark[abs(board[y][x])-1]
                    pygame.draw.circle(screen, color=pygame.Color(colors_light[abs(board[y][x])-1]), center=(x_pos + rect_size/2,y_pos + rect_size/2), radius=20)
                else:
                    text_color = colors_light[abs(board[y][x])-1]
                    pygame.draw.circle(screen, color=pygame.Color(colors_dark[abs(board[y][x])-1]), center=(x_pos + rect_size/2,y_pos + rect_size/2), radius=20)
               
                text = font.render(pieces[abs(board[y][x])][0],True, text_color)
                textRect = text.get_rect()
                textRect.center = (x_pos + rect_size/2,y_pos + rect_size/2)
                
                screen.blit(text, textRect)

            draw_white = not draw_white
            
        draw_white = not draw_white


gameboard = chess_board.GameBoard()

screen = pygame.display.set_mode((screen_size,screen_size))
font = pygame.font.Font('freesansbold.ttf', 24)

from_pos = np.empty(0)
to_pos = np.empty(0)

pygame.init()
running = True

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_focused():
                mouse_pos = (np.array(pygame.mouse.get_pos()) - margin)/rect_size - 0.5
                game_pos = mouse_pos.astype(int)[::-1]

                if from_pos.size == 0:
                    from_pos = game_pos
                elif to_pos.size == 0:
                    to_pos = game_pos
                    if (from_pos.size != 0 and to_pos.size != 0):
                        try:
                            gameboard.move_to(from_pos,to_pos)
                        except Exception as e:
                            print("move error -> reset")
                            print(e)
        
                    from_pos = np.empty(0)
                    to_pos = np.empty(0)

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")
    drawBoard(gameboard.board, side_size)
    # flip() the display to put your work on screen
    pygame.display.flip()

pygame.quit()