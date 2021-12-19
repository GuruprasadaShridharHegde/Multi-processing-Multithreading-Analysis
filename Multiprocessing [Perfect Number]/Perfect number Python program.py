# -*- coding: utf-8 -*-
"""
Created on Sun Dec 19 17:12:53 2021

@author: Guruprasada Shridhar Hegde
"""
# Using a Pool class--->

import time # import the time module
import multiprocessing # import the multiprocessing module

def is_perfect(n):
    sum_factors = 0
    for i in range(1, n): # Range parameter
        if(n % i == 0):
            sum_factors = sum_factors + i
    if (sum_factors == n):
        print('{} is a Perfect number'.format(n))

tic = time.time() # Initialize time for unit test 
pool = multiprocessing.Pool() # Taking pool class
pool.map(is_perfect, range(1,100000)) # Assigning range
pool.close() # Ending pool class
toc = time.time() # get total time to execute the functions

print('Done in {:.4f} seconds'.format(toc-tic)) # print the total time


# Output
# 6 is a Perfect number
# 28 is a Perfect number
# 496 is a Perfect number
# 8128 is a Perfect number
# Done in 74.2217 seconds
# If you compared to a regular for loop we achieved a 71.3% reduction in computation time.



