# fibonacci series:

x = [0, 1]

for n in range(2, 10):
    y = x[n-1] + x[n-2]
    x.append(y)
print(x)


# or:

n1, n2 = 0, 1

for i in range(10):
    if i == 0:
        print(n1)
    elif i == 1:
        print(n2)
    else:
        next = n1 + n2
        print(next)
        n1, n2 = n2, next
