# median serfan ba if
# moghayese 3 tayi hm darim

a = float(input('type 3 numbers\n'))
b = float(input())
c = float(input())

if a > b:
    if a < c:
        median = a
    elif b > c:
        median = b
    else:
        median = c
else:
    if a > c:
        median = a
    elif b < c:
        median = b
    else:
        median = c
print(median)
