num1 = float(input('num1= '))
num2 = float(input('num2= '))
op = input('+,-,*,/ \n')
if op == '+':
    print(num1+num2)
if op == '-':
    print(num1-num2)
if op == '*':
    print(num1*num2)
if op == '/':
    print(num1/num2)

# 1 rah estefade az "eval" hast k miad
# string ro eval mikone khodesh vali
# riskie chon  inpute user mitune taghir bede
# ya hack kone masalan beinesh "" bezare
# code ro kharab kone besh mign
# sql attack

num3 = float(input('num1= '))
num4 = float(input('num2= '))
op2 = input('+,-,*,/ \n')
print(eval(f'{num3}{op2}{num4}'))
