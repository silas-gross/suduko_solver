#!/usr/bin/env python
#coding:utf-8

"""
Each sudoku board is represented as a dictionary with string keys and
int values.
e.g. my_board['A1'] = 8
"""
import time
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
    frow={row+c:board[row+c] for c in COL}
    fc={r+col:board[r+col] for r in ROW}
    for a in frow.keys():
        if frow[a]==i and a != row+col:
            return 0
    for a in fc.keys():
        if fc[a]==i and a !=row+col:
            return 0
    #building the 3x3 square
    r3=[]
    if row in "ABC":
        r3="ABC"
    if row in "DEF":
        r3="DEF"
    if row in "GHI":
        r3="GHI"
    c=int(col)-1
    c=c//3
    c= 3*c+1
    c3=range(c, c+2)
    Square={y+str(z):board[y+str(z)] for y in r3 for z in c3}
    for a in Square.keys():
        if Square[a]==i and a!=row+col:
            return False
    return True
def find_empty(board):
    for i in ROW:
        for j in COL:
            if board[i+j]==0:
                return (i,j)
    return None
def solver(board, t):
    if time.process_time() >= t+575:
        print("could not find solution in proper time")
        return [True, board]
    f=find_empty(board)
    if not f:
        return [True, board]
    for i in range(1,10):
        if forward_check(board, i, f[0], f[1]):
            board[f[0]+f[1]]= i
            if solver(board, t)[0]:
                return [True, board]
            board[f[0]+f[1]]=0
    return [False, board]
    #this takes in the constraints on the particular position and returns the heuristic
    #order of approach will be 1-9 
def backtracking(board,t):
    """Takes a board and returns solved board."""
    # need to implement backtracking here
    #heuristic evaluation broken out into a seperate def
    solved_board = solver(board, t)[1]
    return solved_board


if __name__ == '__main__':
    #  Read boards from source.
    src_filename = 'sudoku_start.txt'
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
        c=board.copy()
        # Print starting board. TODO: Comment this out when timing runs.
        print_board(board)
        ts=time.process_time() # measuring length of solving
        # Solve with backtracking
        solved_board = backtracking(board, ts)
        # Print solved board. TODO: Comment this out when timing runs.
        print_board(solved_board)
        te=time.process_time()
        print("time to run %f" %(te-ts))
        # Write board to file
        outfile.write(board_to_string(solved_board))
        outfile.write('\n')
        #outfile.write("time to solve %f \n" %(te-ts))

    print("Finishing all boards in file.")
