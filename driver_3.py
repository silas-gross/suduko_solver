#!/usr/bin/env python
#coding:utf-8

"""
Each sudoku board is represented as a dictionary with string keys and
int values.
e.g. my_board['A1'] = 8
"""

ROW = "ABCDEFGHI"
COL = "123456789"


def print_board(board):
    """Helper function to print board in a square."""
    print("-----------------")
    for i in ROW:
        row = ''
        for j in COL:
            row += (str(board[i + j]) + " ")
        print(row)


def board_to_string(board):
    """Helper function to convert board dictionary to string for writing."""
    ordered_vals = []
    for r in ROW:
        for c in COL:
            ordered_vals.append(str(board[r + c]))
    return ''.join(ordered_vals)
def forward_check(board, i, row, col):
    frow=[board[row+c] for c in COL]
    fc=[board[r+col] for r in ROW]
    if i in frow:
        return False
    if i in fc:
        return False
    #building the 3x3 square
    r3=[]
    if row in "ABC":
        r3="ABC"
    if row in "DEF":
        r3="DEF"
    if row in "GHI":
        r3="GHI"
    c=col-1
    c=c//3
    c= 3*c+1
    c3=range(c, c+2)
    Square=[board[y+z] for y in r3 for z in c3]
    if i in Square:
        return False
def solver(board):
    f=None
    for i in ROW:
        for j in COL:
            if board[i+j]==0:
                f=[i,j]
    if not f:
        return true
    for i in range(1,10):
        if forward_check(board, i, f[0], f[1]):
            board[f[0]+f[1]]= i
            if eval(board):
                return True
            board[f[0]+f[1]]=0
    return False
    #this takes in the constraints on the particular position and returns the heuristic
    #order of approach will be 1-9 
def backtracking(board):
    """Takes a board and returns solved board."""
    # need to implement backtracking here
    #heuristic evaluation broken out into a seperate def
    solver(board)
    solved_board = board
    return solved_board


if __name__ == '__main__':
    #  Read boards from source.
    src_filename = 'sudokus_start.txt'
    try:
        srcfile = open(src_filename, "r")
        sudoku_list = srcfile.read()
    except:
        print("Error reading the sudoku file %s" % src_filename)
        exit()

    # Setup output file
    out_filename = 'output.txt'
    outfile = open(out_filename, "w")

    # Solve each board using backtracking
    for line in sudoku_list.split("\n"):

        if len(line) < 9:
            continue

        # Parse boards to dict representation, scanning board L to R, Up to Down
        board = { ROW[r] + COL[c]: int(line[9*r+c])
                  for r in range(9) for c in range(9)}

        # Print starting board. TODO: Comment this out when timing runs.
        print_board(board)

        # Solve with backtracking
        solved_board = backtracking(board)

        # Print solved board. TODO: Comment this out when timing runs.
        print_board(solved_board)

        # Write board to file
        outfile.write(board_to_string(solved_board))
        outfile.write('\n')

    print("Finishing all boards in file.")
