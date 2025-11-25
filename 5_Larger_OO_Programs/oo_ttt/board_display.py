x_mark = [r' \/ ', r' /\ ']
o_mark = [r' /\ ', r' \/ ']
empty = ['    ', '    ']

squares = {
    num : empty for num in range(1, 10)
}

def display(squares):
    print()
    print(f'{squares[1][0]}|{squares[2][0]}|{squares[3][0]}')
    print(f'{squares[1][1]}|{squares[2][1]}|{squares[3][0]}')
    print(f'----+----+----')
    print(f'{squares[4][0]}|{squares[5][0]}|{squares[6][0]}')
    print(f'{squares[4][1]}|{squares[5][1]}|{squares[6][1]}')
    print(f'----+----+----')
    print(f'{squares[7][0]}|{squares[8][0]}|{squares[9][0]}')
    print(f'{squares[7][1]}|{squares[8][1]}|{squares[9][1]}')
    print()

# for line in x_mark:
#     print(line)
# for line in o_mark:
#     print(line)

display(squares)