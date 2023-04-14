#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'missingCharacters' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#
import string

def missingCharacters(s):
    # Write your code here

    # Convert the input string to a set of characters
    s_set = set(s)
    # Create a set of all lowercase letters
    letters = set(string.ascii_lowercase)
    # Create a set of all digits
    digits = set(string.digits)
    # Find the difference between the sets of letters and digits and the input set
    missing_letters = letters - s_set
    missing_digits = digits - s_set
    # Return a string that consists of the union of the 
    return "".join(sorted(missing_letters | missing_digits))
    #return "".join(missing_letters | missing_digits)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = missingCharacters(s)

    fptr.write(result + '\n')

    fptr.close()
