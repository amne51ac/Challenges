# -*- coding: utf-8 -*-
"""
Created on Tue May  9 19:35:52 2017

@author: amne51ac

Write a program which takes 2 digits, X,Y as input and generates a 
2-dimensional array. The element value in the i-th row and j-th column of the 
array should be i-1*j-1.
"""

X,Y = input("Please enter an int for Y and X (#,#): ")

print [[i*j for j in range(X)] for i in range(Y)]