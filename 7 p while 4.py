# sum of digits devisable by 13

l1 = [i for i in range(7801, 8853)]
# len(l1) = 1052
l2 = []

for x in l1:
    x = str(x)
    y = int(x[0]) + int(x[1]) + int(x[2]) + int(x[3])
    if y % 13 == 0:
        l2.append(int(x))
print(l2, '\n')

# or sum formula with while:
l3 = []
for y in l1:
    x = y
    sum_digits = 0
    while x:  # ta x sefr beshe yani raghama tamum she edame mide
        sum_digits += x % 10
        x = x//10
    if sum_digits % 13 == 0:
        l3.append(y)
print(l3)
