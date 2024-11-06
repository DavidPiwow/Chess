#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

#define BOARD_SIZE 8 
#define color "\033[0;35m"
#define white "\033[0;m"

struct _board {
    char grid[BOARD_SIZE * BOARD_SIZE];
    char* board_end;
};

struct _move {
	int x1,x2,y1,y2;
};

typedef struct _move Move;
typedef struct _board Board;

typedef int (*validation_function)(Move*);

Board* create_board() {
    Board* temp = (Board*)malloc(sizeof(Board));
    char* board_start = &temp->grid[0];
    temp->board_end = (board_start + BOARD_SIZE * BOARD_SIZE);
	char pieces_u[16] = {'C','N','B','Q','K','B','N','C',
        'P','P','P','P','P','P','P','P'}; 
    char pieces_l[16] = {'p','p','p','p','p','p','p','p',
        'c','n','b','q','k','b','n','c'};

    memset(temp->grid, '0', BOARD_SIZE * BOARD_SIZE);
    memcpy(board_start, pieces_u, sizeof(pieces_u));
    memcpy(temp->board_end - 16, pieces_l, sizeof(pieces_l));
    
    return temp;
}

void print_board(Board* board) {
    char* cur_pos = board->grid;
    printf(color);
    printf("\tA\tB\tC\tD\tE\tF\tG\tH\n\n8\t");
    printf(white);
    
    int row = 7;
    
        while (cur_pos != board->board_end) {
        printf("%c\t", *cur_pos);
        cur_pos++;
        
        if ((cur_pos - board->grid) % BOARD_SIZE == 0) {
            printf(color);
            if (row == 0) {
                printf(white);
                continue;
            }
            printf("\n\n%d\t",row--);
            printf(white);
        }
    }
    printf("\n");
}

static inline char get_piece_at(Board* board, int x, int y) {
    return *(board->grid + x + (y * BOARD_SIZE));
}

static inline void move_piece(Board* board, Move* move) {
    char piece = get_piece_at(board, move->x1, move->x2);
    char* new_pos = board->grid + move->x2 + (move->y2*BOARD_SIZE);
}

int sum_row(Board* board, Move* move) {
    int x_from = (move->x1);
    int x_to = (move->x2);
    int y = (move->y2);
    if (x_to < x_from) {
        int temp = x_from;
        x_from = x_to;
        x_to = temp;
    }
    int sum = 0;
    for (; x_from <= x_to; x_from++) {
        printf("%d ",get_piece_at(board, x_from, y));
        sum += get_piece_at(board, x_from, y);
    }
    return sum;
}

int sum_column(Board* board, Move* move) {
	int x = move->x1;
	int y_from = move->y1;
	int y_to = move->y2;
    if (y_to < y_from) {
        int temp = y_from;
        y_from = y_to;
        y_to = temp;
    }
    int sum = 0;
    for (; y_from <= y_to; y_from++) {
            printf("%c ",get_piece_at(board, x, y_from));
            sum += get_piece_at(board, x, y_from);
    }
    return sum;
}

int check_valid(Board* grid, Move* move) {
	if (move->x1 == move->x2 && move->y1 != move->y2) {
        // column move
    } else if (move->x1 != move->x2 && move->y1 == move->y) {
        // row move
    } else if ((move->x2 - move->x1)/(move->y2-movey1) == 1) {
        // diagona
    }
	return 1;
}

int validate_row() {
	return 0;
} 

void print_column(Board* board, int column) {
    if (column >= BOARD_SIZE) return;
    for (size_t i = 0; i < BOARD_SIZE; i++) {
        printf("%d\n", *(board->grid+i*BOARD_SIZE + column));
    }
}

int num_from_char(char c) {
    if (c >= 'A' && c <= 'Z') {
        return c- 'A';
    }
    if (c >= '0' && c <= '8') {
        return c - '0';
    }
    return -1;
}


Move get_move(void) {
    printf("\nEnter a move(xy -> xy): ");
    char move[9];
    int vars[4];
    int pos = 0;
    if (fgets(move,9,stdin)) {
        for (int i = 0; i <= 9; i++) {
            char cur = move[i];
            if (cur == '-' || cur == '>' || cur == ' ') {
                continue;
            }
            if (cur == '\0') {
                break;
            }
            
            int n = num_from_char(cur);
            
            if (n != -1 && pos <= 4) {
             vars[pos] = num_from_char(cur);
                pos++;
            } else if (pos == 4) {
                break;
            } else {
                
                return get_move();
            }
        }
    }
    printf("%d %d %d %d\n",vars[0],vars[1],vars[2],vars[3]);
    Move x = {vars[0],vars[2],vars[1],vars[3]};
    return x;
}

int main() {
    Board* game_board = create_board();
    print_board(game_board);
	Move move = {0, 0, 5, 0};
    get_move();
    free(game_board);
    
    //system("cls");
    return 0;
}
