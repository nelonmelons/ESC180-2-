'''
 X | O | X
---+---+---
 O | O | X    
---+---+---
   | X | 
'''

import random


def print_board_and_legend(board):
    for i in range(3):
        line1 = " " +  board[i][0] + " | " + board[i][1] + " | " +  board[i][2]
        line2 = "  " + str(3*i+1)  + " | " + str(3*i+2)  + " | " +  str(3*i+3) 
        print(line1 + " "*5 + line2)
        if i < 2:
            print("---+---+---" + " "*5 + "---+---+---")
        
    
    
def make_empty_board():
    board = []
    for i in range(3):
        board.append([" "]*3)
    return board

def squarecord(square_sum):
    coord = [((square_sum - 1) // 3)][(square_sum - 1) % 3]
    return coord
    
def put_in_board(board, mark, square_num):
    coord = squarecord(square_num)
    board[coord[0]][coord[1]] = mark
    
def get_free_squares(board):
    free_squares = []
    for i in range(2):
        for j in range(2):
            if board[i][j] != "O" or "X":
                free_squares.append([i, j])
    return free_squares

def make_random_move(board, mark):
    import random
    free_squares = get_free_squares(board)
    coord = free_squares[int((len(free_squares) * random.random()))]
    board[coord[0]][coord[1]] = mark
    
def is_row_all_marks(board, row_i, mark):
    if board[row_i][0] == board[row_i][1] == board[row_i][2] == mark:
        return True
    elif board[row_i][0] == board[row_i + 1][1] == board[row_i + 2][2] == mark:
        return True
    elif board[row_i][0] == board[row_i - 1][1] == board[row_i - 2][2] == mark:
        return True
    return False         

def is_col_all_marks(board, col_i, mark):
    if board[0][col_i] == board[1][col_i] == board[2][col_i] == mark:
        return True
    elif board[0][col_i] == board[1][col_i + 1] == board[2][col_i + 2] == mark:
        return True
    elif board[0][col_i] == board[1][col_i - 1] == board[2][col_i - 2] == mark:
        return True
    return False
    
def is_win(board, mark):
    if is_row_all_marks(board, mark) == True:
        return True
    elif is_col_all_marks(board, mark) == True:
        return True
    return False

if __name__ == '__main__':
    board = make_empty_board()
    print_board_and_legend(board)    
    
    print("\n\n")
    
    board = [["O", "X", "X"],
             [" ", "X", " "],
             [" ", "O", " "]]
    
    print_board_and_legend(board)  
    count = 0
    input_str = ""
    player = True
    while is_win(board, "X") or is_win(board, "O") == False:
        input_str = input("Enter your move: ")
        free_squares = get_free_squares(board)
        
        
        
        
    
    
                 