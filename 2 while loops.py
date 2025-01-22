x = ['ali', 'reza', 'mahdi', 'danial']
while x:  # ta bool x mosbate mire jelo
    x.pop()
    print(x)

# vaghti pop ro mosavi chizi gharar bedim
# un k pop shode mosavie un mishe na
# liste baghimunde

x1 = ['ali', 'reza', 'mahdi', 'danial']
x2 = x1.pop()
print(x2)


# tu loop ha mese while o for
# mitunim az break o
# continue estefade knim

n = 0
while n < 10:
    print(n)
    if n != 0 and n % 6 == 0:
        break
    n += 1

print('\n')

n = 0
while n < 10:
    print(n)
    if n != 0 and n % 6 == 0:
        n += 2
        continue
    n += 1


# while ham else statement dare
# yani vaghti loop tamum she ejra
# mishe farghesh ba in k bade while
# code benevisim ine k agar khodemun
# while ro break knim dg ejra nmishe
print('\n')

n = 0
while n < 10:
    print(n)
    n += 1
    if n == 2:
        break
else:
    print('loop is done!')
