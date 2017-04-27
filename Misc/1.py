# -*- coding: utf-8 -*-
"""
Created on Wed Apr 26 20:11:16 2017

@author: amne51ac
"""

a = range(2000,3201)
b = []
for i in a:
    if i%7 == 0 and i%5:
        b.append(i)
print b