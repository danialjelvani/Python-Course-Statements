# desired shape:

col = 10
row = 10

base_col = 0
base_row = 0
row_exceptions = [2, 3, 6, 7]

while base_row < row:
    base_col = 1
    if base_row in row_exceptions:
        base_col = 9
    while base_col < col:
        print('*', end=' ')
        base_col += 1
    print('*')
    base_row += 1
