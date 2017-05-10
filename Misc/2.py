# -*- coding: utf-8 -*-
"""
Created on Wed Apr 26 20:27:51 2017

@author: amne51ac

Write a program which can compute the factorial of a given numbers. The results 
should be printed in a comma-separated sequence on a single line. Suppose the 
following input is supplied to the program: 8 Then, the output should be: 40320
"""

a = input("Please enter a number")

for i in range(1,a):
    a = a * i

print a