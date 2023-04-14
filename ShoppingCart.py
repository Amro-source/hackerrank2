#!/bin/python3

import math
import os
import random
import re
import sys



class Item:
    # Implement the Item here
    def __init__(self, name, price):
        self.name = name
        self.price = price

    # Define a method to get the name of the item
    def get_name(self):
        return self.name

    # Define a method to get the price of the item
    def get_price(self):
        return self.price

class ShoppingCart:
    # Implement the ShoppingCart here
    
    def __init__(self):
        self.items = []

    # Define a method to add an item to the shopping cart
    def add(self, item):
        self.items.append(item)

    # Define a method to remove an item from the shopping cart by its name
    def remove_item(self, name):
        # Loop through the items in the shopping cart
        for i in range(len(self.items)):
            # If the name of the item matches the given name
            if self.items[i].get_name() == name:
                # Remove the item from the list
                self.items.pop(i)
                # Break out of the loop
                break
    
    def total(self) :
        # Initialize a variable to store the sum
        total = 0
        # Loop through the items in the shopping cart
        for item in self.items:
        # Add the price of each item to the sum
            total += item.get_price()
            # Return the sum
        return total
    
    def get_count(self) :
        # Return the length of the items list
        return len(self.items)    
    
    
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())
    items = []
    for _ in range(n):
        name, price = input().split()
        item = Item(name, int(price))
        items.append(item)

    cart = ShoppingCart()

    q = int(input())
    for _ in range(q):
        line = input().split()
        command, params = line[0], line[1:]
        if command == "len":
            fptr.write(str(cart.get_count()) + "\n")
        elif command == "total":
            fptr.write(str(cart.total()) + "\n")
        elif command == "add":
            name = params[0]
            item = next(item for item in items if item.name == name)
            cart.add(item)
        else:
            raise ValueError("Unknown command %s" % command)
            
    fptr.close()
