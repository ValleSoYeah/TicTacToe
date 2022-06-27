def check_for_win(board):
    '''Finds out if in our 3 x 3 array there is win and returns a boolean'''
    for i in board: #checks for three same symbols in a row 
        if i.count("X") == 3 or i.count("O") == 3:
            return True
    for c in range(3): #checks for three same symbols in a column 
        if board[0][c] == board[1][c] and board[0][c] == board[2][c]:
            return True
    if board[0][0] == board[1][1] and board[0][0] == board[2][2]: #checks for three symbols in diagonal
         return True
    if board[0][2] == board[1][1] and board[2][0] == board[1][1]: #checks other diagonal 
         return True
    return False


def place_symbol(board, pos, symb): 
    '''Replaces number at indicated index with the player symbol'''
    if type(board[(pos-1)//3][(pos%3)-1]) == int: #checks for type at position 
        board[(pos-1)//3][(pos%3)-1] = symb #converts 1-9 position into array coordinates and replaces with player symbol 
    else:
        print("you cheated, start over") 
        return board, False 
    return board, True

#create board and define player symbol. Converts lowercase symbol into uppercase
board = [[1,2,3],[4,5,6],[7,8,9]] 
print ("",board[0],"\n",board[1],"\n",board[2])
won = False
turn = 0
player1 = input("Player 1, pick your Symbol: ").upper()
if player1 == "X":
    player2 = "O"
elif player1 == "O":
    player2 = "X"
#make sure to only enter symbols X and O 
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
#pick position for player 1      
    placed1 = int(input(f"Player {player1}, place your symbol! ")) 
    if placed1 not in range(1,10):
        print("Position must be a number between 1 and 9")
        placed1 = int(input(f"Player {player1}, place your symbol! "))
    turn += 1
    board, free = place_symbol(board, placed1, player1)
    if free == False: #if player trys to use a taken box, only ONE second chance  
        placed1 = int(input(f"Player {player1}, place your symbol! ")) 
        if placed1 not in range(1,10):
            print("Position must be a number between 1 and 9")
            placed1 = int(input(f"Player {player1}, place your symbol! "))
        board, free = place_symbol(board, placed1, player1)
#after every turn the updated board is printed 
    print ("",board[0],"\n",board[1],"\n",board[2])
    won = check_for_win(board)
    if won == True:
            print(f"Player {player1} has won!")
            break
    elif won == False and turn == 9: #if no one won after turn 9 is a draw 
        print ("It's a draw!")
        break
    #pick position for player 2     
    placed2 = int(input(f"Player {player2}, place your symbol! "))
    if placed2 not in range(1,10):
        print("Position must be a number between 1 and 9")
        placed2 = int(input(f"Player {player2}, place your symbol! "))
    turn += 1
    board, free = place_symbol(board,placed2, player2)
    if free == False: 
        placed2 = int(input(f"Player {player2}, place your symbol! "))
        if placed2 not in range(1,10):
            print("Position must be a number between 1 and 9")
            placed2 = int(input(f"Player {player2}, place your symbol! "))
        board, free = place_symbol(board, placed2, player2)
    print ("",board[0],"\n",board[1],"\n",board[2])
    won = check_for_win(board)
    if won == True:
            print(f"Player {player2} has won!")
            break


