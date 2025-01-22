# conditional job working
# tens digit even do it between 500-1000

num1 = int(input('enter number between 500-1000 \n'))
if 500 <= num1 < 1000:
    x = int(num1/10)
    x2 = x % 10
    if x2 % 2 == 0:
        print('Do it!')
    else:
        print('Dont do it!')

else:
    print('invalid number')
