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
        #print(f"\n{piece_name}@{old_pos} to {new_pos}")

        this.board[old_pos[0],old_pos[1]] = 0
        this.board[new_pos[0],new_pos[1]] = piece
        
        return piece
    
    # make sure a move is legal <3
    def valid_move(this, old_pos, new_pos):
        board_section = this.board[old_pos[0]:new_pos[0]][old_pos[1]:new_pos[1]]

        piece = this.board[old_pos[0]][old_pos[1]]

        # Check if knight and if not ake sure all pieces between are empty 
        if old_pos[0] == new_pos[0] and old_pos[1] != new_pos[1]:
            board_section = this.board[old_pos[0]+1:new_pos[0]]
        elif old_pos[0] != new_pos[0] and old_pos[1] == new_pos[1]: 
            board_section = this.board[old_pos[0]+1:new_pos[0]].T[old_pos[1]]
        elif abs((old_pos[0] - new_pos[0])/(old_pos[1] - new_pos[1])) == 1:
            print("diagonal")
            if (old_pos[0] - new_pos[0])/(old_pos[1] - new_pos[1]) == 1:
                board_section = this.board.diagonal(old_pos[1])[old_pos[0] + 1:new_pos[0]]
            else: 
                board_section = np.fliplr(this.board).diagonal(this.board.shape[1]-1-old_pos[1])[old_pos[0]+1:new_pos[0]]

        print(board_section)

        if board_section.sum() != 0 and piece != 3: 
            print(board_section.sum())
            return False
        

        return True
    
    

b = GameBoard()

def print_wait():
    time.sleep(0.5)
    os.system('cls' if os.name == 'nt' else 'clear')
    print(b.board)
    
os.system('cls' if os.name == 'nt' else 'clear')

#b.move_to((1,3),(2,3))
#b.move_to((1,1),(2,1))


print(b.board)

b.move_to((1,0),(3,0))
print_wait()

b.move_to((0,0),(2,0))
print_wait()

b.move_to((1,1),(2,1))
print_wait()

b.move_to((2,1),(3,1))
print_wait()

b.move_to((2,0),(2,2))
print_wait()

b.move_to((1,3),(2,3))
print_wait()

b.move_to((0,2),(3,5))
print_wait()