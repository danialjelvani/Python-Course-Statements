# check if perfect number:

x = int(input('check if perfect num: '))
sum = 0
while x <= 0:
    print('number is not positive')
    x = int(input('check if perfect num: '))

for i in range(1, x):
    if x % i == 0:
        sum += i
if sum == x:
    print('perfect number!')
else:
    print('not a perfect number!')
