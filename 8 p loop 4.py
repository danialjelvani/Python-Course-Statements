# fun loop

total_row = 5

for i in range(total_row):
    print(' '*(total_row-i), end='')

    for j in range(i+1):
        if j == 0 or j == i:
            element = 1
        else:
            element = element*(i-j+1)/j
        print(int(element), end=' ')
    print()
