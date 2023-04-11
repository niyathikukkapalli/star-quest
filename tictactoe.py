#Tic Tac Toe 

import random 

def drawBoard(board):
    def fromBoard(num):
        return board[num] if board[num] != '' else f'{num}'

    #This function prints out the board that it was passed. 
    #"board" is a list of 10 strings representing the board
    print(f'{fromBoard(7)}|{fromBoard(8)}|{fromBoard(9)}')
    print('-+-+-')
    print(fromBoard(4) + '|' + fromBoard(5) + '|' + fromBoard(6))
    print('-+-+-')
    print(fromBoard(1) + '|' + fromBoard(2) + '|' + fromBoard(3))
#drawBoard(['','','','','','X','','O','','X']). Think of the list as the numbers from 1 - 9. If there 
#is an X in index 4 of board then it will put an X in that index. 

def inputPlayerLetter():
    #Lets the player enter which letter they want to be. X or O?
    #Returns a list with the player's letter as teh first item and the computer's letter as the second. 
    letter = ''
    while not (letter == 'X' or letter == 'O'): #If letter has the value X or O then the loops condition is false.
        #and lets the program execution continue past the while block
        print('Do you want to be X or O?')
        letter = input().upper()

    if letter == 'X':
        return ['X', 'O']
    else: 
        return ['0','X']

def whoGoesFirst(): #the code that calls this dunction will use the return value to determine who will make the first move of the game.
    #Randomly choose which player goes first. 
    if random.randint(0,1) == 0:
        return  'computer'
    else:
        return 'player'

def makeMove(board, letter, move):
    board[move] = letter
    
def isWinner(bo, le):
    #Given a board and a player's letter, this function returns True if that player has won. 
    return ((bo[7] == le and bo[8] == le and bo [9] == le) or
    (bo[4] == le and bo[5] == le and bo [6] == le) or
    (bo[1] == le and bo[2] == le and bo [3] == le) or
    (bo[7] == le and bo[4] == le and bo [1] == le) or
    (bo[8] == le and bo[5] == le and bo [2] == le) or
    (bo[9] == le and bo[6] == le and bo [3] == le) or
    (bo[7] == le and bo[5] == le and bo [3] == le) or
    (bo[9] == le and bo[5] == le and bo [1] == le)) 
    #These are all the possible winning combos that a player could have 
    #Python evaluates all the return values individually. Since it's an or statement only one of the 
    #return statements has to be true for the whole return to be true. 

def getBoardCopy(board):
    #Make a copy of the board list and return it. 
    boardcopy = []
    for i in board: 
        boardcopy.append(i)
    return boardcopy
    #When the AI is plannign its moves it will sometimes need to make modifications to a temporary copy 
    #of the baord without chanigng the actual board. 

def isSpaceFree(board, move):
    #Return true if the passed move is free on the passed board. 
    return board[move] == ''

def getPlayerMove(board):
    #Let the player enter their move. 
    move = ''
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(board, int(move)):
        print('What is your next move? (1-9)')
        move = input()
    return int(move)
    #This function is a short circuit evaluation

def chooseRandomMoveFromList(board, movesList):
    #Returns a valid move from the passed list on the passed board. 
    #Returns non is there is no valid move. 
    possibleMoves = [] #starts as a blank list but the loop iterates over the movesList 
    for i in movesList:
        if isSpaceFree(board,i):
            possibleMoves.append(i)
    if len(possibleMoves) != 0:
        return random.choice(possibleMoves)
    else:
        return None

def getComputerMove(board, computerLetter):
    #Given a board and the computer's etter, determine where to move and return that move.
    if computerLetter == 'X':
        playerLetter = 'O'
    else: 
        playerLetter = 'X'
    #Here is the algorithm for the computer AI
    #First, we check if we can win in the next move. 
    for i in range(1,10):
        boardCopy = getBoardCopy(board)
        if isSpaceFree(boardCopy, i):
            makeMove(boardCopy, computerLetter, i)
            if isWinner(boardCopy, computerLetter):
                return i
    #Check if the player could win on their next move and block them. 
    for i in range(1,10): #iterates the possible moves from 1 to 9 
        boardCopy = getBoardCopy(board)
        if isSpaceFree(boardCopy, i):
            makeMove(boardCopy, playerLetter, i)
            if isWinner(boardCopy, playerLetter):
                return i 
#if the player cannot win in one move then the lop continues past to line 108. 
    #Try to take on the corners if they are free. 
    move = chooseRandomMoveFromList(board, [1,3,7,9])
    if move !=None:
        return move
    #Try to take the center if free 
    if isSpaceFree(board,5):
        return 5
    #if none of the corners are available the code moves onto the center. 
    #move on one of the sides now
    return chooseRandomMoveFromList(board, [2,4,6,8])

def isBoardFull(board):
    #Return true if every space on the board has been taken. Otherwise, return false. 
    for i in range(1,10): 
        if isSpaceFree(board,i):
            return False 
    return True 

#GAME LOOP FINALLYYYY

print('Hi! Here is Tic Tac Toe.... have funnnnn')

while True:
    #Resets the board.
    theBoard = [''] * 10 #the board starts out empty obvi

    playerLetter, computerLetter = inputPlayerLetter() #the computer returns ['X', 'O'] or ['O', 'X'] so the 
    #letters will be in order of the string

    turn = whoGoesFirst()
    print('The' + turn + 'will go first') #the who goes first function returns the string player or computer
    gameIsPlaying = True #keeps track if the game is still playing or if someone has won or tied.

    while gameIsPlaying:
        if turn == 'player': #if this is false it goes past and jumps to the computer 
            #Player's turn
            drawBoard(theBoard)
            move = getPlayerMove(theBoard) #gets the players letter
            makeMove(theBoard, playerLetter, move) #inputs it onto the board 

            if isWinner(theBoard, playerLetter): #the game should check whether the player has won or not
                drawBoard(theBoard)
                print('Hooray! You have won the game!')
                gameIsPlaying = False 
            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print('The game is a tie!')
                    break 
                else:
                   turn = 'computer'
        else: 
            #computer's turn
            move = getComputerMove(theBoard, computerLetter)
            makeMove(theBoard, computerLetter, move)

            if isWinner(theBoard, computerLetter):
                drawBoard(theBoard)
                print('The computer has beaten you! ha loser.')
                gameIsPlaying = False 
            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print('The game is tied')
                    break
                else:
                    turn = 'player'

    print('Do you wanna play again? (yes or no?)')
    if not input().lower().startswith('y'):
        break
