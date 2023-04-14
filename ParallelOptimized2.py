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
    return  math.ceil(file_length / num_cores)
  


def minTime(files, numCores, limit):
    
        # Create a heap of size numCores with initial values of zero
        heap = [0] * numCores
        heapq.heapify(heap)
        # Sort the files in descending order
        files = sorted(files, reverse=True)
        # Initialize a variable to store how many cores are left
        cores_left = numCores
        # Iterate over the files
        for file in files:
            # Pop the smallest element from the heap
            min_work = heapq.heappop(heap)
            # Calculate how many files can be assigned to this core without exceeding its capacity
            files_per_core = math.ceil(min_work / execute_file(file, numCores))
            # If there are more files than cores left
            if len(files) > cores_left:
                # Assign as many files as possible to this core
                files_assigned = min(files_per_core + 1, len(files) - cores_left + 1)
                # Update the min_work by adding the execution time of all assigned files
                min_work += execute_file(file * files_assigned , numCores)
                # Remove the assigned files from the list
                files = files[files_assigned:]
            # Otherwise
            else:
                # Assign only one file to this core
                min_work += execute_file(file , numCores)
                # Remove one file from the list
                files.pop(0)
            # Push the updated element back to the heap
            heapq.heappush(heap , min_work)
            # Update how many cores are left
            cores_left -= 1
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
