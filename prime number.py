# -*- coding: utf-8 -*-
"""
Created on Tue Mar 11 16:33:39 2025

@author: 91912
"""

n = int(input("Enter a number: "))

if n > 1:
    is_prime = 1
    for i in range(2, n):
        if n % i == 0:
            is_prime = 0
            break
    if is_prime == 1:
        print(n, "is a prime number.")
    else:
        print(n, "is not a prime number.")
else:
    print("Please enter a number greater than 1.")
