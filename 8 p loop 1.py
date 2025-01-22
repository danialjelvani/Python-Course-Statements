# check if number

x = input('check if number: ')
nums = set('1234567890')

for char in x:
    if char not in nums:
        print('the string is not a number')
        break
else:
    print('the string is a number')


# rahe 2:

y = input('check if number 2: ')

try:
    float(y)
    print('is a number')
except ValueError:
    print('is not a number')
