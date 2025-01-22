# map krdn:
# map(function, mahale emale func)

def calc_after_tax(price):
    return price*1.2


list1 = [110, 100, 130]
a = list(map(calc_after_tax, list1))
print(a)

list2 = ['ALI', 'HASAN', 'DANIAL']
b = list(map(str.lower, list2))
print(b)

# list comprehension:

list3 = [i*1.2 for i in list1]
print(list3)

list4 = [i.lower() for i in list2]
print(list4)

list5 = [i*1.2 for i in list1 if i > 120]
print(list5)

list6 = [i.lower() for i in list2 if 'D' in i]
print(list6)

list7 = [i.lower() if 'D' not in i else i for i in list2]
print(list7)

list8 = [calc_after_tax(i) for i in list1]
print(list8)

# b ja list mitune set o dictionary ham bashe
# vali tuple comprehension nadarim chon tuple sabete

dict1 = {
    1: 'a',
    2: 'b',
    3: 'c',
}
dict2 = {i*i: x.upper() for i, x in dict1.items()}
print(dict2)

set1 = {i for i in range(5, 20, 2)}
print(set1)
