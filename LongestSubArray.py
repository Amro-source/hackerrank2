#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'longestSubarray' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def longestSubarray(arr):
    # Write your code here

        # Check if the input is an array of integers
        if type(arr) != list or not all(type(x) == int for x in arr):
            # Return an error message
            return "Invalid input. Please enter an array of integers."
    
        # Initialize variables
        max_len = 0 # Maximum length of subarray
        start = 0 # Start index of subarray
        end = 0 # End index of subarray
        count = {} # Dictionary to store the frequency of each value
    
        # Loop through the array
        for i in range(len(arr)):
            # Update the frequency of the current value
            count[arr[i]] = count.get(arr[i], 0) + 1
    
            # If the subarray contains more than two distinct values or the difference between them is more than 1
            while len(count) > 2 or (len(count) == 2 and max(count.keys()) - min(count.keys()) > 1):
                # Reduce the frequency of the value at the start index
                count[arr[start]] -= 1
    
                # If the frequency becomes zero, remove it from the dictionary
                if count[arr[start]] == 0:
                    del count[arr[start]]
    
                # Increment the start index
                start += 1
    
            # Update the end index
            end = i
    
            # Update the maximum length if needed
            max_len = max(max_len, end - start + 1)
    
        # Return the maximum length
        return max_len

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = []

    for _ in range(arr_count):
        arr_item = int(input().strip())
        arr.append(arr_item)

    result = longestSubarray(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
