def check_for_win():
    for i in board:
        columns = []
        if i.count("X") == 3 or i.count("O") == 3:
            return True
    for c in range(3):
        if board[0][c] == board[1][c] and board[0][c] == board[2][c]:
            return True
    if board[0][0] == board[1][1] and board[0][0] == board[2][2]:
         return True
    if board[0][2] == board[1][1] and board[2][0] == board[1][1]:
         return True
    return False


def place_symbol(pos, symb):
    if pos <= 3:
        board[0][pos-1] = symb
    elif pos <= 6:
        board[1][pos-4] = symb
    else:
        board[2][pos-7] = symb
    return board


board = [[1,2,3],[4,5,6],[7,8,9]]
print ("",board[0],"\n",board[1],"\n",board[2])
won = False
turn = 0
player1 = input("Player 1, pick your Symbol: ").upper()
if player1 == "X":
    player2 = "O"
elif player1 == "O":
    player2 = "X"

while player1 != "X" and player1 != "O":
    print("Please choose either X or O")
    player1 = input("Player 1, pick your Symbol: ").upper()
    if player1 == "X":
        player2 = "O"
        break
    elif player1 == "O":
        player2 = "X"
        break
    
        

while won == False:       
    placed1 = int(input(f"Player {player1}, place your symbol! "))
    if placed1 not in range(1,10):
        print("Position must be a number between 1 and 9")
        placed1 = int(input(f"Player {player1}, place your symbol! "))
    turn += 1
    print(turn)
    board = place_symbol(placed1, player1)


    print ("",board[0],"\n",board[1],"\n",board[2])
    won = check_for_win()
    if won == True:
            print(f"Player {player1} has won!")
            break
    elif won == False and turn == 9:
        print ("It's a draw!")
        break
        
    placed2 = int(input(f"Player {player2}, place your symbol! "))
    if placed2 not in range(1,10):
        print("Position must be a number between 1 and 9")
        placed2 = int(input(f"Player {player2}, place your symbol! "))
    turn += 1
    print(turn)
    board = place_symbol(placed2, player2)
    print ("",board[0],"\n",board[1],"\n",board[2])
    won = check_for_win()
    if won == True:
            print(f"Player {player2} has won!")
            break


