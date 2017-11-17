# -*- coding: utf-8 -*-
"""
Created on Tue May  9 18:47:26 2017

@author: amne51ac

Write a program which accepts a sequence of comma-separated numbers from 
console and generate a list and a tuple which contains every number. Suppose 
the following input is supplied to the program: 34,67,55,33,12,98 Then, the 
output should be: ['34', '67', '55', '33', '12', '98'] ('34', '67', '55', '33',
'12', '98')
"""

myList = input("Please enter a comma separated list of values: ")

print list(myList), myList