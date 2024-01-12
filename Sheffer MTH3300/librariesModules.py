#NOTES!!!


# '\r' carriage return resets position to the next line

#slices and range go up a number, not including that last number






string = 'hello world'
integer = 5
floatVar = 2.5
char = '$'
myList = [1, 2, 3]
mySet = {'a','b','c'}
myDict = {'one': 1, 'two': 2, 'three': 3}

print(string,end = '') #prints without a new line at the end

from math import *
import re
import sys
import os
import json
import csv
import shutil

# numpy
import numpy as np

# pandas
import pandas as pd

# string methods
print(string.capitalize())      # capitalizes the first character of the string
print(string.upper())           # converts string to uppercase
print(string.lower())           # converts string to lowercase
print(string.startswith('h'))   # checks if the string starts with 'h'
print(string.endswith('d'))     # checks if the string ends with 'd'
print(string.replace('world', 'universe')) # replaces 'world' with 'universe' in the string
print(string.split())           # splits the string into a list of words
print(string.join(['hello', 'universe'])) # joins a list of words into a single string with the specified delimiter
print(string.strip())           # strips blank lines and spaces from the outsides of the string
print(string.isalpha())         # checks if all characters are in the alphabet

# type conversion
print(int(integer))
print(float(floatVar))
print(str(string))
print(chr(integer))
print(ord(char))

# numeric functions
print(abs(-5))                 # absolute value
print(round(3.14159265359, 2)) # rounds a floating-point number to 2 decimal places
print(pow(2, 3))               # raises a number to the power of another number

# lists
myList.append(0)               # adds an element to the end of the list (will add list but not list elements)
myList.extend([1,2,3])         # adds elements of list to og list 
myList.insert(1, 1.5)          # inserts an element at the specified position
myList.remove(1)               # removes the first occurrence of the specified value
myList.pop()                   # removes the last item in the list
myList.sort()                  # sorts the list in ascending order
myList.reverse()               # reverses the order of the list
print(len(myList))             # returns the number of elements in the list
print(sum(myList))             # returns the sum of all elements in the list
print(min(myList))             # returns the minimum value in the list
print(max(myList))             # returns the maximum value in the list
print(myList.count(1))         # counts the number of occurrences of a value in the list

# sets
mySet.add(4)                   # adds an element to the set
mySet.remove(4)                # removes an element from the set
print(len(mySet))              # returns the number of elements in the set
print(2 in mySet)              # checks if an element is in the set
mySet.clear()                  # removes all elements from the set

# dictionaries
print(myDict.keys())           # returns a view object displaying a list of all the keys in the dictionary
print(myDict.values())         # returns a view object displaying a list of all the values in the dictionary
print(myDict.items())          # returns a view object displaying a list of key-value tuple pairs in the dictionary
print(myDict.get('one'))       # gets the value associated with the specified key
myDict.update({'four': 4})     # updates the dictionary with the

# Create a numpy array from myList
np_array = np.array(myList)

# essential attributes
print(string.__class__)        # returns the class of the object
print(myList.__len__())        # returns the number of elements in the list (same as len(myList))
print(myDict.__getitem__('one')) # gets the value associated with the specified key (same as myDict['one'])

# Special methods (dunder/magic methods)
__init__ # Constructor method; initializes a new object of a class
__str__  # Returns a human-readable string representation of an object
__repr__ # Returns a string representation of an object suitable for debugging
__eq__   # Compares two objects for equality
__ne__   # Compares two objects for inequality
__lt__   # Compares two objects for less than
__le__   # Compares two objects for less than or equal to
__gt__   # Compares two objects for greater than
__ge__   # Compares two objects for greater than or equal to
__add__  # Defines how objects should be added using the + operator
__sub__  # Defines how objects should be subtracted using the - operator
__mul__  # Defines how objects should be multiplied using the * operator
__truediv__ # Defines how objects should be divided using the / operator
__floordiv__ # Defines how objects should be divided using the // operator
__mod__  # Defines how objects should be modulo-ed using the % operator
__pow__  # Defines how objects should be exponentiated using the ** operator

# built-in functions
print(type(string))            # returns the type of the object
print(isinstance(string, str)) # checks if the object is an instance of a specified class
print(hasattr(myList, 'append')) # checks if the object has a specified attribute
print(getattr(myList, 'append')) # gets the value of a specified attribute
print(callable(getattr(myList, 'append'))) # checks if the attribute is callable (e.g., a method)

# Accessing attributes of custom objects
class MyClass:
    x = 5

my_obj = MyClass()
print(my_obj.x)                # accesses the 'x' attribute of the object



class myClass:
    __init__
    __name__="theClass"
    def sayName():
        print(__name__)
        

