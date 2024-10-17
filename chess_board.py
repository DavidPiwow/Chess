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

# type 1 == white // type -1 == black
def check_pawn(type, old_pos, new_pos):
        pass

class GameBoard:
    def __init__(this, side_size=8):
        # Initialize empty board
        this.board = np.full((side_size, side_size), 0)

        # Place pawns
        this.board[1] = -1
        this.board[-2] = 1

        # Place other pieces (negative for black pieces)
        this.board[0]  = -1 * row
        this.board[-1] = row[::-1] 
    
    def piece_at(this, row, col):
        return this.board[row][col]
    
    # start move process
    def move_to(this, old_pos, new_pos):
        
        if this.valid_move(old_pos,new_pos) == False:
            return
        
        piece = this.piece_at(old_pos[0],old_pos[1])
        piece_name = pieces[piece]
        print(f"\n{piece_name}@{old_pos} to {new_pos}")

        this.board[old_pos[0],old_pos[1]] = 0
        this.board[new_pos[0],new_pos[1]] = piece
        
        return piece
    
    # make sure a move is legal <3
    def valid_move(this, old_pos, new_pos):
        piece = this.board[old_pos[0]][old_pos[1]]

        # Check if knight and if not ake sure all pieces between are empty 
        if abs(piece) == 3:
            pass
        
        elif abs(new_pos[0] - old_pos[0]) == 0 or abs(new_pos[1] - old_pos[1] == 0):
            # horizontal move
            if new_pos[0] == old_pos[0] and new_pos[1] != old_pos[1]:
                # horizontal
                move_type = 0
                start = old_pos[1]
                end = new_pos[1]
                move_distance = start-end

                if (abs(piece) == 6 and move_distance > 1) or not (abs(piece) == 2 or abs(piece) >= 5):
                    print(piece)
                    return False 
                
            elif old_pos[0] != new_pos[0] and old_pos[1] == new_pos[1]:
                # vertical
                if not (abs(piece) == 2 or abs(piece) == 1 or abs(piece) >= 5):
                    
                    return False
            
                move_type = 1
                start = old_pos[0]
                end = new_pos[0]
                move_distance = start-end

                if (abs(piece) == 6 or abs(piece) == 1 and move_distance > 1):
                    
                    return False

            flip = False

            if start > end:
                temp = start
                start = end
                end = temp 
                flip = True

            if move_type == 0:
                if not flip:
                    board_section = this.board[new_pos[0]][start+1:end+1]
                else:
                    board_section = this.board[new_pos[0]][start+1:end]
            else:
                if not flip:
                    board_section = this.board.T[new_pos[1]][start+1:end+1]
                else:
                    board_section = this.board.T[new_pos[1]][start+1:end]
                
        elif abs((old_pos[0] - new_pos[0])/(old_pos[1] - new_pos[1])) == 1:
            # positive diagonal
            if abs(piece) < 4:
                return False

            if (old_pos[0] - new_pos[0])/(old_pos[1] - new_pos[1]) == 1:
                board_section = this.board.diagonal(old_pos[1])[old_pos[0] + 1:new_pos[0]+1]
            # negative diagonal
            else: 
                board_section = np.fliplr(this.board).diagonal(this.board.shape[1]-1-old_pos[1])[old_pos[0]+1:new_pos[0]+1]

        if board_section.sum() != 0 and piece != 3:
            print(board_section)
            first = board_section[board_section != 0][-1]
            if (first * piece) > 0 or this.piece_at(new_pos[0],new_pos[1]) != first:
                return False
        

        return True
    
  
