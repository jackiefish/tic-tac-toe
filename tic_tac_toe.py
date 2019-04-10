# The player who is playing "X" always goes first.

def choose_x_or_o():
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

def play():
    print('Position is shown as follow:')
    n = 0
    my_list = [[1,2,3],[4,5,6],[7,8,9]]
    print_list(my_list)

    print('\'X\' represents move of player 1, \'O\' represents move of player 2')
    for m in range(1,10):
        if m%2 == 0:
            #even move -> player 2
            # print(f'Player 2 please choose position of your move')
            m_2 = int(input(f'Player 2 please choose position of your move: '))
            if m_2 in range(1,4):
                my_list[0][m_2-1] = 'O'
                # if m > 5:
                #     if my_list[0]
            elif m_2 in range(4,7):
                my_list[1][m_2 - 4] = 'O'
            elif m_2 in range(7,10):
                my_list[2][m_2 - 7] = 'O'
        else:
            #odd move -> player 1
            m_1 = int(input(f'Player 1 please choose position of your move: '))
            if m_1 in range(1,4):
                my_list[0][m_1-1] = 'X'
            elif m_1 in range(4,7):
                my_list[1][m_1 - 4] = 'X'
            elif m_1 in range(7,10):
                my_list[2][m_1 - 7] = 'X'

        print_list(my_list)
        while m > 5:
            # 8 lines in total that need check
            if my_list


def print_list(lst):
    for i in range(1,8):
        if not i%2 == 0:
            # odd row 1,3,5,7
            print('+---+---+---+')
        else:
            for item in lst[int(i/2) - 1]:
                print(f'| {item} ', end ="")
            print('|')

play()
