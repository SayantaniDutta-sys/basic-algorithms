# -*- coding: utf-8 -*-
"""
Created on Tue Mar 11 17:11:08 2025

@author: 91912
"""

n = int(input("Enter a number: "))
sum = 0  
temp = n    
while temp > 0:  
    digit = temp % 10  
    sum += digit ** 3   
    temp //= 10  

if sum == n:  
    print("Armstrong Number")  
else:  
    print("Not an Armstrong Number")