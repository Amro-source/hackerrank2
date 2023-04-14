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

# Define a function that returns the execution time for a file
def execute_file(file_length, num_cores):
  # If the file length is divisible by the number of cores
  if file_length % num_cores == 0:
    # Return the file length divided by the number of cores
    return int(file_length / num_cores)
  # Otherwise
  else:
    # Return the file length
    return file_length



def minTime(files, numCores, limit):
    # Write your code here

    execution_times = Parallel(n_jobs=limit)(delayed(execute_file)(file, numCores) for file in files)
    # Sum up the execution times for all files
    total_time = sum(execution_times)
    # Return the total time
    return total_time
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
