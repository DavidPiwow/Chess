from enum import Enum
import numpy as np
import os, time

class PieceType(Enum):
    Empty = 0
    Pawn = 1
    Castle = 2
    Knight = 3
    Bishop = 4
    Queen = 5
    King = 6

pieces = ["Empty","Pawn","Castle","Knight","Bishop","Queen","King"]

row = np.array([2,3,4,5,6,4,3,2])

class GameBoard:
    def __init__(this, side_size=8):
        # Initialize empty board
        this.board = np.full((side_size, side_size), 0)

        # Place pawns
        this.board[1] = -1
        this.board[-2] = 1

        # Place other pieces (negative for black pieces)
        this.board[0]  = -1 * row
        this.board[-1] = row 
    
    def piece_at(this, row, col):
        return this.board[row][col]
    
    # start move process
    def move_to(this, old_pos, new_pos):
        
        if this.valid_move(old_pos,new_pos) == False:
            return
        
        piece = this.piece_at(old_pos[0],old_pos[1])
        piece_name = pieces[abs(piece)]
        
        print(f"\n{piece_name}@{old_pos} to {new_pos}")

        this.board[old_pos[0],old_pos[1]] = 0
        this.board[new_pos[0],new_pos[1]] = piece
        
        return piece
    
    def check_knight(this, old_pos, new_pos):
        move_x = abs(new_pos[0] - old_pos[0])
        move_y = abs(new_pos[1] - old_pos[1])
        if  not ((move_x == 2 and move_y == 1) or (move_x == 1 and move_y == 2)):
            return False
        # if its not negative * positive return false
        if (this.piece_at(old_pos[0],old_pos[1]) * this.piece_at(new_pos[0],new_pos[1])) > 0:
            return False
                
        return True

    # make sure a move is legal <3
    def valid_move(this, old_pos, new_pos):
        piece = this.board[old_pos[0]][old_pos[1]]
        new_piece = this.board[new_pos[0],new_pos[1]]

        if piece * new_piece > 0:
            return False
        
        # Check if knight and if not ake sure all pieces between are empty 
        if abs(piece) == 3:
            return this.check_knight(old_pos, new_pos)
        
        # check if its a horizontal or vertical move  
        elif abs(new_pos[0] - old_pos[0]) == 0 or abs(new_pos[1] - old_pos[1] == 0):
            if new_pos[0] == old_pos[0] and new_pos[1] != old_pos[1]:
                # horizontal
                if (abs(piece) == 1): 
                    return False
                move_type = 0
                start = old_pos[1]
                end = new_pos[1]
                
            elif old_pos[0] != new_pos[0] and old_pos[1] == new_pos[1]:
                # vertical
                move_type = 1
                start = old_pos[0]
                end = new_pos[0]
            
            move_distance = start-end
            # u better be the right piece
            if (abs(piece) == 6 and move_distance > 1) or not (abs(piece) == 1 or abs(piece) == 2 or abs(piece) >= 5):
                return False 

            flip = False
            if start > end:
                
                start,end = end,start
                flip = True


            if move_type == 0:
                if not flip:
                    board_section = this.board[new_pos[0]][start+1:end+1]
                else:
                    board_section = this.board[new_pos[0]][start:end]
            else:
                if not flip:
                    board_section = this.board.T[new_pos[1]][start+1:end+1]
                else:
                    board_section = this.board.T[new_pos[1]][start:end]
                
        elif abs((old_pos[0] - new_pos[0])/(old_pos[1] - new_pos[1])) == 1:
            # diagonal
            if abs(piece) < 4 and abs(piece != 1):
                return False
            
            if abs(piece) == 1:
                if new_pos[0] != old_pos[0] - piece:
                    return False
                
            board_section = []

            f_row = old_pos[0]
            f_col = old_pos[1]
            n_row = new_pos[0]
            direction = 1

            if f_row > n_row:
                direction = -1

            for i in range(1,abs(old_pos[0] - new_pos[0])):
                board_section.append(this.piece_at(f_row + i * direction, f_col + i*direction))

            board_section = np.array(board_section)
            
        non_zeroes = board_section[board_section != 0]

        if  non_zeroes.size > 0:
            if non_zeroes.size == 1 and non_zeroes[0] == new_piece and  non_zeroes[0] * piece < 0:
                return True
            return False
        
        return True
    
  
