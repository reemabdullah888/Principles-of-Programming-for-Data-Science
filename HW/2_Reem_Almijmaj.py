# -*- coding: utf-8 -*-
"""
Created on Fri Nov  5 22:47:06 2021

@author: lenovo
"""

def read_csv(filename):
    file_name = open (filename,encoding='utf-8-sig')
    item = [line.rstrip().split(',')for line in file_name] #remove the \n at the end of the line, and split each time it counters ,
    header = item [0] #fist row
    value = item [1:] #to take from the header and forward.
    d = {}
    for i in range (len(header)):
        d[header[i]] = [row[i] for row in value] #store the header as the key, and the values as a list of value to the key.
    return (d)

