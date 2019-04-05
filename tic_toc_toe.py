def tic_toc_toe():
    player_1 = input('Player 1, please choose from \'O\' and \'X\': ')

    while True:
        if player_1.lower() == 'o':
            player_1 = player_1.upper()
            player_2 = 'X'
            break
        elif player_1.lower() == 'x':
            player_1 = player_1.upper()
            player_2 = 'O'
            break
        else:
            player_1 = input('Player 1, Please choose from \'O\' and \'X\': ')

    print(f'Player 1 will use \'{player_1}\' and Player 2 will use \'{player_2}\'.')

tic_toc_toe()
