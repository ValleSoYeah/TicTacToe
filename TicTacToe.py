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

        print("This box is taken!")
        return board, False 
    return board, True


# Create board and define player symbol. Converts lowercase symbol into uppercase

board = [[1,2,3],[4,5,6],[7,8,9]] 
print ("",board[0],"\n",board[1],"\n",board[2])
won = False
turn = 0
player1 = input("Player 1, pick your Symbol: ").upper()
if player1 == "X":
    player2 = "O"
elif player1 == "O":
    player2 = "X"

# Make sure only symbols X and O are entered

while player1 != "X" and player1 != "O":
    print("Please choose either X or O") 
    player1 = input("Player 1, pick your Symbol: ").upper()
    if player1 == "X":
        player2 = "O"
        break
    elif player1 == "O":
        player2 = "X"
        break
    

# Let the game begin!         
while won == False:  
    # Player 1 chooses position      
    placed1 = int(input(f"Player {player1}, place your symbol! ")) 
    while placed1 not in range(1,10):
        print("Position must be a number between 1 and 9")
        placed1 = int(input(f"Player {player1}, place your symbol! "))
    turn += 1
    board, free = place_symbol(board, placed1, player1) #place symbol at chosen position 
    while free == False: #Insist on valid position

        placed1 = int(input(f"Player {player1}, place your symbol! ")) 
        if placed1 not in range(1,10):
            print("Position must be a number between 1 and 9")
            placed1 = int(input(f"Player {player1}, place your symbol! "))
        board, free = place_symbol(board, placed1, player1)

    
    print ("",board[0],"\n",board[1],"\n",board[2]) #After every turn the updated board is printed 
    won = check_for_win(board) #did this turn win the game?
    if won == True:
            print(f"Player {player1} has won!")
            break
    # If no one won after turn 9 it is a draw
    elif won == False and turn == 9:  
        print ("It's a draw!")
        break
    
    #Player 2 picks position     

    placed2 = int(input(f"Player {player2}, place your symbol! "))
    while placed2 not in range(1,10):
        print("Position must be a number between 1 and 9")
        placed2 = int(input(f"Player {player2}, place your symbol! "))
    turn += 1

    board, free = place_symbol(board,placed2, player2) #place symbol at chosen position
    while free == False:  #Insist on valid position

        placed2 = int(input(f"Player {player2}, place your symbol! "))
        if placed2 not in range(1,10):
            print("Position must be a number between 1 and 9")
            placed2 = int(input(f"Player {player2}, place your symbol! "))
        board, free = place_symbol(board, placed2, player2)
    print ("",board[0],"\n",board[1],"\n",board[2])

    won = check_for_win(board) #did this turn win the game?

    if won == True:
            print(f"Player {player2} has won!")
            break


