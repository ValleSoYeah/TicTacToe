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

def play_turn(board, player):
    '''Plays the turn for the specified player'''
    placed = int(input(f"Player {player}, place your symbol! ")) 
    while placed not in range(1,10):
        print("Position must be a number between 1 and 9")
        placed = int(input(f"Player {player}, place your symbol! "))
    new_board, free = place_symbol(board, placed, player) #place symbol at chosen position 
    while free == False: #Insist on valid position
        placed = int(input(f"Player {player}, place your symbol! ")) 
        if placed not in range(1,10):
            print("Position must be a number between 1 and 9")
            placed = int(input(f"Player {player}, place your symbol! "))
        new_board, free = place_symbol(board, placed, player)
    print ("",board[0],"\n",board[1],"\n",board[2]) #After every turn the updated board is printed 
    won = check_for_win(board) #did this turn win the game?
    return new_board, won

def assign_symbols():            
    '''Asks for user input and returns the two chosens symbols'''
    sym1 = input("Player 1, pick your Symbol: ").upper()
    if sym1 == "X":
        sym2 = "O"
    elif sym1 == "O":
        sym2 = "X"
    
    while sym1 != "X" and sym1 != "O": # Make sure only symbols X and O are entered
        print("Please choose either X or O") 
        sym1 = input("Player 1, pick your Symbol: ").upper()
        if sym1 == "X":
            sym2 = "O"
            break
        elif sym1 == "O":
            sym2 = "X"
            break
    return sym1, sym2

# Create board and assign player symbol
board = [[1,2,3],[4,5,6],[7,8,9]] 
print ("",board[0],"\n",board[1],"\n",board[2])
won = False
turn = 0
player1, player2 = assign_symbols()
    
#Let the game begin!         
while won == False:  
    board, won = play_turn(board, player1)
    if won == True:
        print(f"Player {player1} has won!")
        break
    turn += 1
    
    if turn == 9:  
        print ("It's a draw!")
        break
    board, won = play_turn(board, player2)
    
    if won == True:
        print(f"Player {player2} has won!")
        break
    turn += 1
    


