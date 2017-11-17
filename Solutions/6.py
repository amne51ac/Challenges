# -*- coding: utf-8 -*-
"""
Created on Tue May  9 19:25:33 2017

@author: amne51ac

Write a program that calculates and prints the value according to the given 
formula: Q = Square root of [(2 * C * D)/H] Following are the fixed values of C
and H: C is 50. H is 30. D is the variable whose values should be input to your
program in a comma-separated sequence.
"""


print [(((2*50*D)/30)**0.5) for D in input("Please enter a comma separated \
list of numbers: ")]