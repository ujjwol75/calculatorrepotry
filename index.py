board = [['_', '_', '_'],
         ['_', '_', '_'],
         ['_', '_', '_']]

def board_display(board):
    for i in range(3):
        print()
        for j in range(3):
            print(board[i][j], end=' ')
            if j < 2:
                print('|', end=' ')


def user_input():
    global pos
    pos = input("\nEnter any value (0 to 9): ")
    pos = int(pos) -  1
    if pos <= 9:
        return pos
    else:
        pos = input("\nEnter the value between 0 to 9: ")
        pos = int(pos) - 1
        
    
def board_input_display(pos, player):
    row = pos // 3
    column = pos % 3
    if board[row][column] == '_':
        board[row][column] = player
    elif board[row][column] == player:
        print("You already did")
    return 1


# i = 0
# def better_board(board):
#     global i
#     j = 0
#     while (j<=2):
#         print(board[i][j])
#         j = j+1
#     i = i+1    

def check_row(i):
    x = 0
    y = 0
    for j in range(3):
        if board[i][j] == 'X':
            x += 1
        if board[i][j] == 'O':
            y += 1

    if x == 3:
        print("X won")
        return game_on == False
    elif y == 3:
        print("O won")
        return game_on == False
    else:
        return game_on == True

def check_column(i):
    x = 0
    y = 0
    for j in range(3):
        if board[j][i] == 'X':
            x += 1
        if board[j][i] == 'O':
            y += 1

    if x == 3:
        print("X won")
        return game_on == False
    elif  y == 3:
        print("O won")
        return game_on == False
    else:
        return game_on == True

def check_diagonal(a,b,c):
    var = [a, b, c]
    x = 0
    y = 0
    for i in var:
        if i == 'X':
            x += 1
        if i == 'O':
            y += 1

    if x == 3:
        print('X won')
        return game_on == False

    elif y == 3:
        print("O won")
        return game_on == False

    else:
        return game_on == True

def game_tie():
    for i in range(3):
        for j in range(3):
            if board[i][j] == '_':
                return 
            else:
                continue
    print("Game is tie.")
    return game_on == False

def main():
    global game_on 
    game_on = True
    count = 1
    
    # better_board(board)
    board_display(board)
    while game_on:
        if count % 2 == 0:
            player = 'X'  
        else:
            player = 'O'
            
        pos = user_input()
        board_input_display(pos, player)
        count = count + board_input_display(pos, player)
        for i in range(3):
            game_on = check_row(i)
            game_on = check_column(i)
        game_on = check_diagonal(board[0][0],board[1][1],board[2][2])
        game_on = check_diagonal(board[0][2],board[1][1],board[2][0])
        
        print(board_display(board))

        game_tie()

    


main()
