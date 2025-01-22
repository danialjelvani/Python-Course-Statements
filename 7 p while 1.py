# look for artists sales and update:

artist_sales = {
    'andy': 100,
    'arash': 50,
    'ebi': 800,
}
artist_name = input('enter artist name: ')

while artist_name != 'exit':
    if artist_name in artist_sales:
        print(artist_sales[artist_name])
    else:
        x = input('''
        artist name not in the library!
        if u like to update the list,
        please enter the number
        of album sales: ''')
        artist_sales.update({artist_name: x})
        print(artist_sales)

    artist_name = input('enter artist name: ')

print('exited')
