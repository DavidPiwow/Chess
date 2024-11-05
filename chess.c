#include <stdio.h>
#include <stdlib.h>

#define BOARD_SIZE 8 

struct _board {
    int grid[BOARD_SIZE * BOARD_SIZE];
    int* board_start;
    int* board_end;
};

struct _move {
	int x1,x2,y1,y2;
};

typedef struct _move Move;
typedef struct _board Board;
typedef int (*validation_function)(*Move);

Board* create_board() {
    Board* temp = (Board*)malloc(sizeof(Board));
    temp->board_start = &temp->grid[0];
    temp->board_end = (temp->board_start + BOARD_SIZE * BOARD_SIZE);
	char pieces_u[8] = ['C','N','B','Q','K','B','N','C']; 
    char pieces_l[8] = ['c','n','b','q','k','b','n','c'];
    int* cur_pos = temp->board_start;
    int i = 1;
    //int z = 10;
    while (cur_pos != temp->board_end) {
       *cur_pos = i; //(cur_pos - temp->board_start) % BOARD_SIZE + z;
       cur_pos++;
       i++;
       //if (i++ % 10 == 0) z += 10;
    }
	
    return temp;
}

void print_board(Board* grid) {
    int* cur_pos = grid->board_start;
     while (cur_pos != grid->board_end) {
        printf("%2d ", *cur_pos);
        cur_pos++;
        if (((cur_pos - grid->board_start) % BOARD_SIZE) == 0) {
            printf("\n");
        }
    }
}

static inline int get_piece_at(Board* grid, int x, int y) {
    return *(grid->board_start + x + (y * BOARD_SIZE));
}

int sum_row(Board* grid, Move* move) {
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
        printf("%d ",get_piece_at(grid, x_from, y));
        sum += get_piece_at(grid, x_from, y);
    }
    return sum;
}

int sum_column(Board* grid, Move* move) {
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
            printf("%d ",get_piece_at(grid, x, y_from));
            sum += get_piece_at(grid, x, y_from);
    }
    return sum;
}

int check_valid(validation_function func, Board* grid) {
	
	return 1;
}

int validate_row() {
	
} 

void print_column(Board* grid, int column) {
    if (column >= BOARD_SIZE) return;
    for (size_t i = 0; i < BOARD_SIZE; i++) {
        printf("%d\n", *(grid->board_start+i*BOARD_SIZE + column));
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
