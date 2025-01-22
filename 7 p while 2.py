# simple calc:

x = 0
msg = 'enter number to add: '
num = input(msg)

while num != 'total':
    x = x + float(num)
    num = input(msg)

print(f'total is = {x}')
