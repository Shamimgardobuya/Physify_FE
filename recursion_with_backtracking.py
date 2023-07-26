#using recursion find factorial of a number
#base case number is less 1 or equal to 1return number
#repeated action is the number multiplied to it's previous(n-1) *(n)
def find_factorial(number):
    if number == 1 or number < 1:  #base case was okay
        return number
    #one comparison 
   
    else:
       return number * find_factorial(number - 1)  #sub action to be repeated was number * function(number -1) initially didn't get what we want
        #2 multiplication and subtraction
        #time complexity - 3 0n same as with space complexity 
print(find_factorial(9))


global size
size = 4
def printSolution(chess_board):
    for i in range(size):
        for j in range(size): #i row and j column
            print(chess_board[i][j],end=' ')
        print()



#lets test but first we place the queen anywhere then check all rows then columns, then rows and then positive and negative diagonal
def check_safety_queen(chessboard,row, col):
    #check if row is lef side
    for i in range(col):
        if chessboard[row][i]  == 1:
            return False
    #check upper diagonal on left side
    #negative diagonal
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if chessboard[i][j] == 1:
            return False
        
    #check lower diagonal on left side
    #positive diagonal
    for i, j in zip(range(row, size, 1), range(col, -1, -1)):
        if chessboard[i][j] == 1:
            return False
    
    return True

def solveQueen(chessboard, col): #recursion to repeat the particular task and till fill all the boxes Queen can fill without attacking each other
    if col >=size:
        return True
    
    for i in range(size):
        if check_safety_queen(chessboard,i, col):
            chessboard[i][col]
            if solveQueen(chessboard,col + 1) == True:
                return True
            chessboard[i][col] = 0


    return False

def solution():
    chessboard = [ [0, 0, 0, 0],
                   [0, 0, 0, 0],
                   [0, 0, 0, 0],
                   [0, 0, 0, 0],
                   ]


    if solveQueen(chessboard, 0 )== False:
        print("Solution does not exist")
        return False
    
    printSolution(chessboard)
    return True
solution()
    
    

    
    



