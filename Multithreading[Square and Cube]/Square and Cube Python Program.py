# -*- coding: utf-8 -*-
"""
Created on Sun Dec 19 17:43:27 2021

@author: Guruprasada Shridhar Hegde
"""

import time # import time module  
import threading  
from threading import *  
def cal_sqre(num):  # define a square calculating function  
    print(" Calculate the square root of the given number")  
    for n in num: # Use for loop   
        time.sleep(0.3)  # at each iteration it waits for 0.3 time  
        print(' Square is : ', n * n)  
  
def cal_cube(num): # define a cube calculating function  
    print(" Calculate the cube of  the given number")  
    for n in num: # for loop  
        time.sleep(0.3) # at each iteration it waits for 0.3 time  
        print(" Cube is : ", n * n *n)  
ar = [8, 3, 4, 11, 21] # given array  
t = time.time() # get total time to execute the functions  
#cal_cube(ar)  
#cal_sqre(ar)  
th1 = threading.Thread(target=cal_sqre, args=(ar, ))  
th2 = threading.Thread(target=cal_cube, args=(ar, ))  
th1.start()  
th2.start()  
th1.join()  
th2.join()  
print(" Total time taking by threads is :", time.time() - t) # print the total time for unit Test 
print(" Again executing the main thread")  
print(" Thread 1 and Thread 2 have finished their execution.")  
# Output
#Calculate the square root of the given number
#Calculate the cube of  the given number
#Cube is 512 :  Square is :  64
#Cube is 9 :  Square is :  27
#quare is 16 :  Cube is :  64
#Cube is 1331 :  Square is :  121
#Square is 441 : Cube is :  9261
#Total time taking by threads is : 1.5584020614624023
#Again executing the main thread
#Thread 1 and Thread 2 have finished their execution.
