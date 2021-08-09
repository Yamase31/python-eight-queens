"""
Authors: James Lawson and Beth Ann Townsend
Project 5
File name: eightQueens.py
This is a program that finds a solution to the "Eight Queens" logic problem so
that all queens on the chessboard are safe from attacks from one another. The
program, upon calculating a solution, prints the outcome.
"""
def main():
    import math
    #starts queens at same position to later be moved
    board = [0, 0, 0, 0, 0, 0, 0, 0]

    #this is what makes the "board" visible on the screen
    def printBoard():
        for row in range (len(board)):
            print("  |  ", end="")
            for column in range(len(board)):
                if row == board[column]:
                    print("Q |  ", end="")
                else: print("  |  ", end="")
            print()

    #rowTestPassed = False
    #diagTestPassed = False

    def changeRow(queen):
        for i in range(queen + 1, len(board)):
            if board[i] == board[queen]:
                board[queen] += 1
                board[queen] = board[queen]%7
        return True

    def checkRow():
        rowcount = 0
        for item in board:
            if item == row:
                rowcount += 1
        if rowcount != 1:
            return False
        else:
            return True

    def changeDiagonal(queen):
        for i in range(queen + 1, len(board)):
            difference = abs(queen - i)
            dia = board[queen] + difference
            diag = board[queen] - difference
            if board[i] == dia or board[i] == diag:
                board[queen] += 1
                board[queen] = board[queen]%7
        return True
    
    #this is supposed to iterate over the row and diagonal changes and then print when safe
    def checkSafe():
        #while loop instead?
        for i in range(100000):
            changeRow(7)
            changeDiagonal(7)
            changeRow(6)
            changeDiagonal(6)
            changeRow(5)
            changeDiagonal(5)
            changeRow(4)
            changeDiagonal(4)
            changeRow(3)
            changeDiagonal(3)
            changeRow(2)
            changeDiagonal(2)
            changeRow(2)
            changeRow(1)
            changeDiagonal(1)
            changeRow(0)
            changeDiagonal(0)
        printBoard()
    checkSafe()
    

if __name__ == "__main__":
    main()
