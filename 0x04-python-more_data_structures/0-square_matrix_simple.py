#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    rows = len(matrix)
    cols = len(matrix[0])
    
    squared_m = []
    for i in range(rows):
        squared_row = []
        for j in range(cols):
            squared_row.append(matrix[i][j] ** 2)
        squared_m.append(squared_row)
    
    return squared_m

