# -*- coding: utf-8 -*-
"""
Created on Fri Nov  5 23:19:48 2021

@author: lenovo
"""

import sys
import csv
if __name__== "__main__":
    input_file = sys.argv[1]
    output = sys.argv[2]




def transpose(input_file, output = 'output.csv'):
    file = open(input_file, encoding='utf-8-sig')
    reader = csv.reader(file)
    element = [line.rstrip().split(',') for line in file] #remove the last \n and split when ever it counter a , 
    
    rows = len(element) # we take the length of the element as the number of rows
    columns = len(element[0]) # length of the fist element in element which represent the number of columns
    
        
    transpose = [[element[i][j] for i in range(rows)] for j in range(columns)]     # By using double indexing we find the  transpose 
#    
    
    output_file = open(output, 'w') # Open csv file for writing 
    output_writer = csv.writer(output_file, delimiter = ',') # creating a csv writer object
    
    for r in transpose:
        output_writer.writerow(r) # writing the transposed csv file 
        
    return transpose