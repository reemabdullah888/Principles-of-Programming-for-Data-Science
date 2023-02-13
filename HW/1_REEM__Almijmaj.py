# -*- coding: utf-8 -*-
"""
Created on Fri Nov  5 22:30:54 2021

@author: lenovo
"""

def Absolute_values(list):
    l = []
    r = []
    for item in list: #itererate through the list item by item
        if type(item) is int: #test if the items has data type = integer 
            l.append(int(item))
        elif type(item) is float: #test if the items has data type = float 
            l.append(float(item))
        elif type(item) is str: #test if the items has data type = string 
            if '.' in item: # to check the decimal part data type
                try:
                    l.append(float(item))
                except ValueError:
                    continue 
            else:
                try:
                    l.append(int(item))  # to check the decimal part data type
                except ValueError:
                    continue
    for element in l:
        r.append(abs(element))  # to append the absolute value of a number
    return r


Absolute_values(["DSCI-510", -1, 0.1, 2, "US", 3, "-3"] )

