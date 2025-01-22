# mini program:
# pip install termcolor tu terminal

from termcolor import colored

name_list = ['danial']
msg = colored('''
0   quit
1   check if i know u
2   introduce urself to me
3   make me forget u
4   print a list of people i know                                                                                                        
''', 'yellow')
welcome_note = input(msg)

while welcome_note != '0':
    if welcome_note == '1':
        username = input('enter ur name plz: ')
        if username in name_list:
            print('i know u')
        else:
            print('i dont know u')
    welcome_note = input(msg)

    if welcome_note == '2':
        new_name = input('introduce urself: ')
        if new_name in name_list:
            print('i already know u')
        else:
            name_list.append(new_name)
            print('now i know u')
    if welcome_note == '3':
        saved_name = input('enter ur name to forget: ')
        if saved_name in name_list:
            name_list.remove(saved_name)
            print('now i dont know u')
        else:
            print('i already didnt know u')
    if welcome_note == '4':
        print(name_list)
print('u exited the bot')
