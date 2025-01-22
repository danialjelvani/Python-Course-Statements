# desired shape

col = 10
row = 5

current_col = 0
current_row = 0

while current_row < row:
    current_col = 0
    if current_row == 4:
        current_col = 5
    while current_col < col:
        print('*', end=' ')
        current_col += 1
    current_row += 1
    print('*')
