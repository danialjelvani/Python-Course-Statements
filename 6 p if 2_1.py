# the weekday name

dic = {
    '1': 'shanbe',
    '2': '1 shanbe',
    '3': '2 shanbe',
    '4': '3 shanbe',
    '5': '4 shanbe',
    '6': '5 shanbe',
    '7': 'jome',
}
day_num = input('enter days number: ')
for key, value in dic.items():
    if key == day_num:
        print(value)

# or

print(dic[day_num])
