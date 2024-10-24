#--------------WINNING CONFIGURATIONS------------
winning_config = [[1,2,3], [4,5,6], [7,8,9], [1,4,7], [2,5,8], [3,6,9], [1,5,9], [3,5,7]]

#----------------BOARD-----------------
rows = ['   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ']
row_empty = '-----------'

def display_board(rows):
        print(f'{rows[0]}|{rows[1]}|{rows[2]}')
        print(row_empty)
        print(f'{rows[3]}|{rows[4]}|{rows[5]}')
        print(row_empty)
        print(f'{rows[6]}|{rows[7]}|{rows[8]}')


print(' 1 | 2 | 3 ')
print('-----------')
print(' 4 | 5 | 6 ')
print('-----------')
print(' 7 | 8 | 9 ')

#----------------PLAYERS---------------
list_x = []
list_o = []
print('Choose a square you want take by typing an appropriate numer.')
display_board(rows)

#-------------CHECKING IF THERE IS A WINNER---------------
def checking_for_winner(positions):
    for winning in winning_config:
        triple = 0
        for element in positions:
            if element in winning:
                triple += 1
        if triple == 3:
            return True
    return False

#---------------PLAYER TURN --------------------
def player_turn(positions, player):

    all_positions = list_x + list_o
    correct_input = False

    while not correct_input:
        choice = int(input(f"Player '{player.capitalize()}', choose your square: "))
        if choice in all_positions:
            print('This square is already taken')
        else:
            positions.append(choice)
            if player == 'x':
                rows[choice - 1] = ' x '
            elif player == 'o':
                rows[choice - 1] = ' o '
            display_board(rows)
            correct_input = True


while True:

    player_turn(positions=list_x, player='x')
    if checking_for_winner(list_x) == True:
        print("Player 'X' is a winner!")
        break
    elif len(list_x + list_o) == 9:
        print("It's a draw!")
        break

    player_turn(positions=list_o, player='o')
    if checking_for_winner(list_o) == True:
        print("Player 'O' is a winner!")
        break

