#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'numCells' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY grid as parameter.
#

def numCells(grid):
    # Write your code here

    res = 0 # initialize the result
    for i in range(len(grid)): # loop over the rows
        for k in range(len(grid[0])): # loop over the columns
            val = grid[i][k] # get the current cell value
            flag = 1 # initialize a flag to indicate dominance
            for ii in range(max(0,i-1), min(len(grid),i+2)): # loop over the neighboring rows
                for kk in range(max(0,k-1), min(len(grid[0]),k+2)): # loop over the neighboring columns
                    if ii != i or kk != k: # skip the current cell
                        if grid[ii][kk] >= val: # compare the neighbor value with the current value
                            flag = 0 # set the flag to 0 if the neighbor is equal or greater
                            break # break out of the inner loop
                if flag == 0: # break out of the outer loop if the flag is 0
                    break
            if flag == 1: # if the flag is still 1, then the cell is dominant
                res += 1 # increment the result
    return res # return the result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grid_rows = int(input().strip())
    grid_columns = int(input().strip())

    grid = []

    for _ in range(grid_rows):
        grid.append(list(map(int, input().rstrip().split())))

    result = numCells(grid)

    fptr.write(str(result) + '\n')

    fptr.close()
