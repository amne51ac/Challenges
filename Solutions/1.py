# -*- coding: utf-8 -*-
"""
Created on Wed Apr 26 20:11:16 2017

@author: amne51ac

Write a program which will find all such numbers which are divisible by 7 but 
are not a multiple of 5, between 2000 and 3200 (both included). The numbers 
obtained should be printed in a comma-separated sequence on a single line.
"""

a = range(2000,3201)
b = []
for i in a:
    if i%7 == 0 and i%5:
        b.append(i)
print b