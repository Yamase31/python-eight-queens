"""
Authors: James Lawson and Beth Ann Townsend
Project 5
File name: eightQueens.py
"""

#put in main

#def boardDisplay():







import math



#def randomNumbers




#for loop

#i = index

#all queen are at spot 1 and then they are changed out one by 1, row by row

board = [0,1,2,3,4,5,6,7]

print(board)

def printBoard ():
    for row in range (len(board)):
        print("  |  ", end="")
        for column in range(len(board)):
            if row == board[column]:
                print("Q |  ", end="")
            else: print("  |  ", end="")
        print()

#board = [1,2,3,4,5,6,7,8]

printBoard()

#def checkRow


#def changeBoard(row, column):

rowTestPassed = False
diagTestPassed = False


def checkRow():
    if board[0] == board[1] or board[0] == board[2] or board[0] == board[3] or board[0] == board[4] or board[0] == board[5] or board[0] == board[6] or board[0] == board[7]:
        board[0] += 1
        rowTestPassed = False
        if board[0] > 7:
            board[0] = board[0]%7
    else:
        rowTestPassed = True

    if board[1] == board[0] or board[1] == board[2] or board[1] == board[3] or board[1] == board[4] or board[1] == board[5] or board[1] == board[6] or board[1] == board[7]:
        board[1] += 1
        rowTestPassed = False
        if board[1] > 7:
            board[1] = board[1]%7
    else:
        rowTestPassed = True

    if board[2] == board[0] or board[2] == board[1] or board[2] == board[3] or board[2] == board[4] or board[2] == board[5] or board[2] == board[6] or board[2] == board[7]:
        board[2] += 1
        rowTestPassed = False
        if board[2] > 7:
            board[2] = board[2]%7
    else:
        rowTestPassed = True

    if board[3] == board[0] or board[3] == board[1] or board[3] == board[2] or board[3] == board[4] or board[3] == board[5] or board[3] == board[6] or board[3] == board[7]:
        board[3] += 1
        rowTestPassed = False
        if board[3] > 7:
            board[3] = board[3]%7
    else:
        rowTestPassed = True

    if board[4] == board[0] or board[4] == board[1] or board[4] == board[2] or board[4] == board[3] or board[4] == board[5] or board[4] == board[6] or board[4] == board[7]:
        board[4] += 1
        rowTestPassed = False
        if board[4] > 7:
            board[4] = board[4]%7
    else:
        rowTestPassed = True

    if board[5] == board[0] or board[5] == board[1] or board[5] == board[2] or board[5] == board[3] or board[5] == board[4] or board[5] == board[6] or board[5] == board[7]:
        board[5] += 1
        rowTestPassed = False
        if board[5] > 7:
            board[5] = board[5]%7
    else:
        rowTestPassed = True

    if board[6] == board[0] or board[6] == board[1] or board[6] == board[2] or board[6] == board[3] or board[6] == board[4] or board[6] == board[5] or board[6] == board[7]:
        board[6] += 1
        rowTestPassed = False
        if board[6] > 7:
            board[6] = board[6]%7
    else:
        rowTestPassed = True

    if board[7] == board[0] or board[7] == board[1] or board[7] == board[2] or board[7] == board[3] or board[7] == board[4] or board[7] == board[5] or board[7] == board[6]:
        board[7] += 1
        rowTestPassed = False
        if board[7] > 7:
            board[7] = board[7]%7
    else:
        rowTestPassed = True
        

        

        

    #x = 0
    #y = 1
    #board[0] = x
    #board[1] = x+2
    #board[2] = x+4
    #board[3] = x+6

    #board[4] = y+2
    #board[5] = y+4
    #board[6] = y+6

    #x += 1
        #if board[x] == board[x+2
    

#here the numbers should be [7,6,5,4,3,2,1,0]
#I think the system that I am thinking of can work if we run it a ton of times
def checkDiagonal():
    if board[0] == board[0] + 1 or board[0] == board[0] - 1:
        board[0] += 1
        diagTestPassed = False
        if board[0] > 7:
            board[0] = board[0]%7
    else:
        diagTestPassed = True

    if board[1] == board[0] + 1 or board[1] == board[0] - 1 or board[1] == board[2] + 1 or board[1] == board[2] + 1:
        board[1] += 1
        diagTestPassed = False
        if board[1] > 7:
            board[1] = board[1]%7
    else:
        diagTestPassed = True

    if board[2] == board[1] + 1 or board[2] == board[1] - 1 or board[2] == board[3] + 1 or board[2] == board[3] -1:
        board[2] += 1
        diagTestPassed = False
        if board[2] > 7:
            board[2] = board[2]%7
    else:
        diagTestPassed = True

    if board[3] == board[2] + 1 or board[3] == board[2] - 1 or board[3] == board[4] + 1 or board[3] == board[4] - 1:
        board[3] += 1
        diagTestPassed = False
        if board[3] > 7:
            board[3] = board[3]%7
    else:
        diagTestPassed = True

    if board[4] == board[3] + 1 or board[4] == board[3] - 1 or board[4] == board[5] + 1 or board[4] == board[5] - 1:
        board[4] += 1
        diagTestPassed = False
        if board[4] > 7:
            board[4] = board[4]%7
    else:
        diagTestPassed = True

    if board[5] == board[4] + 1 or board[5] == board[4] - 1 or board[5] == board[6] + 1 or board[5] == board[6] - 1:
        board[5] += 1
        diagTestPassed = False
        if board[5] > 7:
            board[5] = board[5]%7
    else:
        diagTestPassed = True

    if board[6] == board[5] + 1 or board[6] == board[5] - 1 or board[6] == board[7] + 1 or board[6] == board[7] - 1:
        board[6] += 1
        diagTestPassed = False
        if board[6] > 7:
                board[6] = board[6]%7
    else:
        diagTestPassed = True

    if board[7] == board[6] - 1 or board[7] == board[6] + 1:
        board[7] += 1
        diagTestPassed = False
        if board[7] > 7:
            board[7] = board[7]%7
    else:
        diagTestPassed = True
    
    

    
#def checkDiagonal(row1, row2, column1, column2):
    #if (abs(row1-row2)) == (abs(column1-column2)):
        #return False

def checkBoard():
    for j in range(100000):
    #while rowTestPassed == False or diagTestPassed == False:
        checkRow()
        checkDiagonal()




#def findSolutions    
#each of the 8 for loops in range 8  


