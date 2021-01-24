## Matrix Manipulation
import random
import sys

def updateMatrix(matrix):
    # Make this global variable for all functions
    mat = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    
    for i in range (len(matrix)):
        for j in range (len(matrix)):
            mat[i][j] = matrix[i][j]
    return mat
    

def print_matrix(matrix):
    """
    This function increases the length of 'x' to 5 characters and fill the end with spaces.
    This will help to allign different values of the array and allow the matrix to look neater overall.     
    """
    for i in range(len(matrix)):
        line = ""
        for j in range(len(matrix)):
            line += str(matrix [i][j]).rjust(5)
        print("\r" + line)
    print("\r")

def score(matrix):
    score = 0

    for i in range (len(matrix)):
        for j in range (len(matrix)):
            score += matrix[i][j]

    return score

def addNum(matrix):

    """
    This function adds a new 2 or 4 to the grid. This will happen twice to set the game up and then once
    each time a swipe is performed
    """
    
    # Find a random i and j coordinate to add 2 or 4
    randi = random.randint(0, len(matrix) - 1)
    randj = random.randint(0, len(matrix) - 1)
    # Create a random integer from 3 possibilities 
    randInt = random.randint(0, 3)
    # If a random entry in the matrix is 0
    if matrix[randi][randj] == 0:
        
        if randInt == 0 or randInt == 1:
            # 66.6% chance of a 2
            matrix[randi][randj] = 2
        else:
            # 33.3% chance of a 4
            matrix[randi][randj] = 4
    else:
        # If the delegated matrix entry does not equal 0, run the function again and again until a 0 entry is found
        addNum(matrix);

    
def transpose(matrix):
    tr_mat = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

    for i in range (len(matrix)):
        for j in range (len(matrix[0])):
            tr_mat[j][i] = matrix[i][j]

    return tr_mat


def rotateLeft(matrix):
    left_mat = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    tr_mat = transpose(matrix)
    
    for i in range (len(matrix)):
        for j in range (len(matrix)):
            left_mat[i][j] = tr_mat[3 - i][j]

    return left_mat

def rotateRight(matrix):
    right_mat = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    tr_mat = transpose(matrix)

    for j in range (len(matrix)):
        for i in range (len(matrix)):
            right_mat[i][j] = tr_mat[i][3 - j]

    return right_mat

def swipeUp(matrix):
 
    k = 0
    # For each column
    for j in range(0,len(matrix)):
        # Each row minus the first
        for i in range(1,len(matrix)):

            # if an element doesn't equal zero
            if matrix[i][j] != 0:
                # Equate the row of the non-zero element to a new variable (k)
                k = i
                # whilst the row is not at the top of the matrix and the there is a zero element above it
                while (k > 0) & (matrix[k - 1][j] == 0):
                    # move the row up
                    matrix[k - 1][j] = matrix[k][j]
                    # Fill in the gap with a new zero
                    matrix[k][j] = 0
                    # Increment the row number downwards
                    k = k - 1
    

    # for each column
    for j in range(0, len(matrix)):
        # for each row minus the last
        for i in range(0, len(matrix) - 1):
            # if the element is non-zero and if the same column in row below has an equal number

            if (matrix[i][j] != 0) & (matrix[i][j] == matrix[i+1][j]):
                # Add the two elements together
                matrix[i][j] = matrix[i][j] + matrix[i + 1][j]
                # Create a new zero element below upon addition
                matrix[i + 1][j] = 0
                # For rows below similar numbers
                for k in range(i + 2, len(matrix) - 1):
                    # move up the other rows
                    matrix[k - 1][j] = matrix[k][j]
                    # Fill vacated rows with zeros
                    matrix[k][j] = 0
                    #print_matrix(matrix)

    addNum(matrix);
        
    return matrix

def swipeRight(matrix):
    left = rotateLeft(matrix)
    up = swipeUp(left)
    originalMatrix = rotateRight(up)
    
    return originalMatrix

def swipeLeft(matrix):
    right = rotateRight(matrix)
    up = swipeUp(right)
    originalMatrix = rotateLeft(up)

    return originalMatrix

def swipeDown(matrix):
    left = rotateLeft(matrix)
    left = rotateLeft(left)
    up = swipeUp(left)
    right = rotateLeft(up)
    originalMatrix = rotateLeft(right)
    return originalMatrix


