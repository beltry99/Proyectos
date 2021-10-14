# -*- coding: utf-8 -*-
"""
Created on Thu Oct 14 13:17:18 2021

@author: jaime
"""

import random
import pyautogui
import numpy as np
import time


chars = "1234567890"
chars_list = list(chars)

password = pyautogui.password("Enter a pin code: ")

results = []
stopwatch = []

for i in range(2000):
    guess_password = ""
    number = 0
    start_time = time.perf_counter()
    
    while(guess_password != password):
        guess_password = random.choices(chars_list, k=len(password))
    
        number +=1
        
        if(guess_password == list(password)):
            break
    end_time = time.perf_counter()
    stopwatch.append(end_time-start_time)
    results.append(number)
    

print(np.mean(stopwatch))
print(np.mean(results))
