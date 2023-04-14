#!/bin/python3

import math
import os
import random
import re
import sys


class Multiset:

    def __init__(self):
        # initialize an empty dictionary to store the elements and their counts
        self.elements = {}
    
    def add(self, val):
        # adds one occurrence of val from the multiset, if any
        self.elements[val] = self.elements.get(val, 0) + 1
        

    def remove(self, val):
        # removes one occurrence of val from the multiset, if any
        if val in self.elements and self.elements[val] > 0:
            self.elements[val] -= 1
            if self.elements[val] == 0:
                del self.elements[val]

    def __contains__(self, val):
        # returns True when val is in the multiset, else returns False
        
        return val in self.elements and self.elements[val] > 0
        
    
    def __len__(self):
        # returns the number of elements in the multiset
    
        return sum(self.elements.values())
if __name__ == '__main__':
    def performOperations(operations):
        m = Multiset()
        result = []
        for op_str in operations:
            elems = op_str.split()
            if elems[0] == 'size':
                result.append(len(m))
            else:
                op, val = elems[0], int(elems[1])
                if op == 'query':
                    result.append(val in m)
                elif op == 'add':
                    m.add(val)
                elif op == 'remove':
                    m.remove(val)
        return result

    q = int(input())
    operations = []
    for _ in range(q):
        operations.append(input())

    result = performOperations(operations)
    
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')
    fptr.close()
