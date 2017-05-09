# -*- coding: utf-8 -*-
"""
Created on Wed Apr 26 20:34:53 2017

@author: amne51ac
"""

a = input("Please type an integer: ")
b = {}

for i in range(1,a+1):
    b[i] = i**2

print b

squareRange = lambda x: {i:i**2 for i in range(1,x+1)}