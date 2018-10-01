# row = col
# col = 4-row
# n = sqrt(len(string))

from math import sqrt

def row_col_from_index(index,n):
    row = index//n
    col = index % n
    return (row,col)

def get_new_row_col(row,col,n):
    row_new = col
    col_new = n-1-row
    return (row_new,col_new)

def get_n(string):
    return int(sqrt(len(string)))

def index_from_row_col(row,col,n):
    return row*n+col

for i in range(int(input().strip())):
    str_i = [i for i in input().strip()]
    str_o = [i for i in str_i]
    n = get_n(str_i)
    for index,char in enumerate(str_i):
        row,col = row_col_from_index(index,n)
        row,col = get_new_row_col(row,col,n)
        index_new = index_from_row_col(row,col,n)
        str_o[index_new]=char
    print(''.join(str_o)[::-1])
