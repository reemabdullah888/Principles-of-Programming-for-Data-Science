# -*- coding: utf-8 -*-
"""
Created on Fri Nov  5 23:11:15 2021

@author: lenovo
"""

def trasformation(filename):
    dic_ = read_csv (filename)
    trans_d ={}
    for k in dic_: #loop throuth the dictionary 
        new_key = dic_[k][-1] #to take the last value of the last key of the dictionary 
        trans_d[new_key] = dic_[k][0:-1] 
        trans_d[new_key].insert(0,k) #add the value as key to the dictionary. 
        
    return trans_d