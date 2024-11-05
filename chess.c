#include <stdio.h>
#include <stdlib.h>

#define BOARD_SIZE 8 

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
	char pieces_u[16] = {'C','N','B','Q','K','B','N','C','P','P','P','P','P','P','P','P'}; 
    char pieces_l[16] = {'p','p','p','p','p','p','p','p','c','n','b','q','k','b','n','c'};

    memset(temp->grid, 0, BOARD_SIZE * BOARD_SIZE * sizeof(int));
    memcpy(board_start, pieces_u, sizeof(pieces_u));
    memcpy(temp->board_end - 16, pieces_l, sizeof(pieces_l));
    
    return temp;
}

void print_board(Board* board) {
    char* cur_pos = board->grid;
    while (cur_pos != board->board_end) {
        printf("%c ", *cur_pos);
        cur_pos++;
        if (((cur_pos - board->grid) % BOARD_SIZE) == 0) {
            printf("\n");
        }
    }
}

static inline char get_piece_at(Board* board, int x, int y) {
    return *(board->grid + x + (y * BOARD_SIZE));
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

int check_valid(validation_function func, Board* grid) {
	
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

int main() {
    Board* game_board = create_board();
    print_board(game_board);
    //print_column(game_board, 1);
    
	Move move = {0, 0, 5, 0};
    printf("\n%d\n", sum_column(game_board, &move));
    free(game_board);
    //system("cls");
    return 0;
}
