# -*- coding: utf-8 -*-
"""
Created on Tue Mar 11 16:31:43 2025

@author: 91912
"""

n = int(input("Enter a natural number: "))

if n > 0:
    total = 0
    for i in range(1, n + 1):
        total += i
    print(f"The sum of natural numbers from 1 to {n} is: {total}")
else:
    print("Please enter a positive integer.")