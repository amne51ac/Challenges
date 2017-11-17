# -*- coding: utf-8 -*-
"""
Created on Tue May  9 19:06:08 2017

@author: amne51ac

Define a class which has at least two methods: getString: to get a string from 
console input printString: to print the string in upper case. Also please 
include simple test function to test the class methods.
"""

class myClass():
    
    def __init__(self):
        self.inValue = ''
    
    def getString(self):
        self.inValue = str(raw_input("Please type a string: "))
    
    def printString(self):
        print self.inValue.upper()
    
    
if __name__ == "__main__":
    myObject = myClass()
    myObject.getString()
    myObject.printString()