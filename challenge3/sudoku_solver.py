"""
solve using backtracking
it is a list of lists, where each inner list is a row in our sudoku puzzle
return whether a solution exists
"""
import numpy as np
grid = [[5, 3, 0, 0, 7, 0, 0, 0, 0],  #we need more empty field to get more solution
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 0, 0]]

print(np.array(grid))
print("\n")


def possible(row, column, number):
    global grid
    #is the number appearing in d row
    for i in range(0, 9):
        if grid[row][i] == number:
            return False

    #is the number appearing in the column
    for i in range(0, 9):
        if grid[i][column] == number:
            return False

    #is d number appearing in the given square
    """
    row0, row3, row6--> starting pt of square
    row0-row2 --> section0
    row3-row5 --> section1
    row6-row8 --> section2
    """
    x_0 = (column // 3) * 3
    y_0 = (row // 3) * 3 #starting pt of square
    for i in range(0, 3):  #row in square, 0, 1, 2
        for j in range(0, 3):  #column in square
            if grid[y_0+i][x_0+j] == number:
                return False

    return True  #if d number doesnt appear in row, column and square


def solve():
    global grid
    for row in range(0, 9):
        for column in range(0, 9):
            if grid[row][column] == 0:  #empty space, stopping condition wnen no zero
                for number in range(1, 10): #0-9
                    if possible(row, column, number):
                        grid[row][column] = number
                        solve()  #call it recursively
                        grid[row][column] = 0 #if its stuck, if not valid reset to 0
                return

    print(np.array(grid))
    input("More possible solutions")  #cclick enter in terminal


solve()

