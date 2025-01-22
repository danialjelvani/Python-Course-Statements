# conditional sum

a = float(input('enter 3 scores\n'))
b = float(input())
c = float(input())
mean = (a+b+c)/3
if 16 < mean < 20:
    print('final score is: 20')
else:
    print('final score is:', round(mean, 2))
