#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'minTime' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY files
#  2. INTEGER numCores
#  3. INTEGER limit
#
from joblib import Parallel, delayed
import math
import heapq

def execute_file(file_length, num_cores):
    # If the file length is divisible by the number of cores
    # Return the file length
    #return  math.ceil(file_length / num_cores)
    file_size=file_length
    # Check if file size is divisible by num cores and limit is not exceeded
    if file_size % num_cores == 0 and file_size / num_cores <= limit:
    # Return file size divided by num cores
        return math.ceil(file_size / num_cores)
    # Otherwise
    else:
        # Return file size as it is
        return file_size
    
def find_max(resultlist):
    maxval = max(map(max, resultlist))
    return maxval    


def minTime(files, numCores, limit):
          # Create a heap of size num_cores with initial values of zero
    heap = [0] * numCores
    heapq.heapify(heap)
    # Sort the files in descending order
    files = sorted(files, reverse=True)
    # Initialize a counter for the number of files executed in parallel
    count = 0
    # Iterate over the files
    for file in files:
        # Pop the smallest element from the heap
        min_work = heapq.heappop(heap)
        # Add the execution time of the file to the min_work
        min_work += execute_file(file, numCores)
        # Push the updated element back to the heap
        heapq.heappush(heap, min_work)
        # If the file was executed in parallel
        if file % numCores == 0:
            # Increment the counter
            count += 1
            # If the limit is reached
            if count == limit:
                # Break out of the loop
                break
    # Return the largest element in the heap as the total time
    return max(heap)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    files_count = int(input().strip())

    files = []

    for _ in range(files_count):
        files_item = int(input().strip())
        files.append(files_item)

    numCores = int(input().strip())

    limit = int(input().strip())

    result = minTime(files, numCores, limit)

    fptr.write(str(result) + '\n')

    fptr.close()
