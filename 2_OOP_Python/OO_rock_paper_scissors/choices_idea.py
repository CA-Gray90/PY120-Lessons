d = {
    ('r', 'rock') : 'Its a rock choice',
    ('p', 'paper') : 'Its a paper choice'
}

choice = input('input r or p: ')
for key in d.keys():
    if choice in key:
        print(d[key])