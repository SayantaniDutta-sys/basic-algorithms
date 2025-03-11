# -*- coding: utf-8 -*-
"""
Created on Tue Mar 11 16:48:45 2025

@author: 91912
"""

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a > b and a > c:
    max_value = a
elif b > c:
    max_value = b
else:
    max_value = c

print("The maximum value is:", max_value)