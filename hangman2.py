import random 
#added 2 more guesses in this version
HANGMAN_PICS = [''' 

+----+
     |
     |
     |
     |
     |
   =====

''', 

''' 
 +----+
 0    |
      |
      |
      |
      |
      |
    =====

''', 

''' 
 +----+
 0    |
 |    |
      |
      |
      |
      |
    =====
''', 

''' 
 +----+
 0    |
/|    |
      |
      |
      |
      |
    =====
''', 

''' 
 +----+
 0    |
/|\   |
      |
      |
      |
      |
    =====
''', 

''' 
 +----+
 0    |
/|\   |
/     |
      |
      |
      |
    =====
''', 

''' 
 +----+
 0    |
/|\   |
/ \   |
      |
      |
      |
    =====
''',
''' 
 +----+
[0    |
/|\   |
/ \   |
      |
      |
      |
    =====
''',''' 
 +----+
[0]   |
/|\   |
/ \   |
      |
      |
      |
    =====
''']
#used dictionaries 
words = {'deserts': 'icecream donut cake apple pecan pudding cookie cookies tiramisu crumble brulee mousse tarts cheesecakes baubles biscuits chocolate flipz reeses snickers musketeers affogato macaroon sunade popsicle jello eclair brownie cupcake pancakes pie'.split(), 
'colors':'red orange yellow green blue indigo purple violet white black magenta lilac lavender chestnut brown'.split(), 
'subjects':'math philosophy science english art astronomy biology physics geography history geometry calculus chemistry latin french spanish'.split(), 
'countries':'armenia australia mexico bulgaria germany russia india china egypt tazmania nigeria argentinia bolivia netherlands france sweden switzerland norway finland mongolia'.split()}
#a lot easier to write then all the stuff with commas and spaces

def getRandomWord(wordDict):
    #This func will return a single secret word from the list in wordList
    #First randomly select a key from the dictionary:
    #A key is the thing in the apostrophes to the left of the colon
    wordKey = random.choice(list(wordDict.keys()))
    #Second, randomly choose a word from the key's list in the dictionary: 
    wordIndex = random.randint(0, len(wordDict[wordKey]) - 1) 
    #chooses a word from the list above, len counts the number of items in the list 
    #wordList is our parameter: we replace it with words when we actaully call this function
    return [wordDict[wordKey][wordIndex], wordKey]
    
def displayBoard(missedLetters, correctLetters, secretWord):
    print(HANGMAN_PICS[len(missedLetters)])
    print()

    #missedLetters = letters not in the word
    #correctLetters = letters in the word
    #secret word = the word
    #HANGMANPICS is a global variable and has a list of strings for every type of board. Ex. If missedLetters is 'aetr' then len(missedLetters)
    #will return 4 so it will display HANGMANPICS[4]

    print('Missed letters:', end='')
    for letter in missedLetters:
        print(letter, end='')
    print()
        #the end = '' is adding spaces. if the missedLetters were abcd the for loop prints a b c d

    blanks = '_ ' * len(secretWord) #displays the _ _ _ _ _ layout

    for i in range(len(secretWord)): #Replaces the blanks with the correctly guessed letters. the range makes the for loop go through all the indexes.  
         if secretWord[i] in correctLetters:
            blanks = blanks[:i] + secretWord[i] + ' ' + blanks[i+1:] #uses list slicing. We want blanks from the beginning of hte lits ot the correct letter 
            # then the correct letter and then the rest of the blanks from the correct letter ot the end of the list

    for letter in blanks: 
        print(letter, end='') #show the secret word with spaces in between each letter 
    print() #why this random print thing? 

def getGuess(alreadyGuessed):
        #python is case sensitive so we need to make sure the player enters a lowercase letter
        #alreadyGuessed is the string of letters that the player has already guessed
        # .lower() method returns a string with all lowercase letters. .upper() does similarly. 

        while True: #since the condiiton is only True the only way to exit the loop is by a break 
            print('Guess a letter.')
            guess = input()
            guess = guess.lower()
            if len(guess) !=1:
                print('please enter a single letter answer')
            elif guess in alreadyGuessed:
                print('you have already guessed that letter. choose again dumbo')
            elif guess not in 'abcdefghijklmnopqrstuvwxyz':
                print('do you know what a letter is bro')
            else:
                return guess 

def playAgain():
        #This function retuns True if the player wants to play again
        print('Do you want to play again (yes or no')
        return input().lower().startswith('y') #basically the player can enter like yes, YES, Y, or y and that would mean yes. 

print('H-A-N-G-M-A-N') #first print call that executes when the game is run
missedLetters = '' #blank string is assigned since the player didnt do anything yet 
correctLetters = ''
secretWord, secretSet = getRandomWord(words) #will randomly choose a word 
gameIsDone = False #will be True when the player doesnt want to play again

while True:
    print('The secret word is in the set: ' + secretSet)
    displayBoard(missedLetters, correctLetters, secretWord)
    #Let the player guess a letter.
    guess = getGuess(missedLetters + correctLetters) 

    if guess in secretWord:
        correctLetters = correctLetters + guess #new value of correctLetters 
        #Check if the player has won

        foundAllLetters = True #starts by asumming that the player has guessed all the letters 
        for i in range(len(secretWord)):
            if secretWord[i] not in correctLetters:
                foundAllLetters = False #the program runs through all the letters and if it finds a letter that is not in correctLetters then then the 
            #player has not found all the letters.
                break

        if foundAllLetters: #will only print if foundAllLetters is true 
            print('Yes! The Secret word is "' + secretWord + '"! You have won!')
            gameisDone = True

    else: 
         missedLetters = missedLetters + guess #so if the guess is not in the secret word then it becomes a missed letter. 

    #Check if the player has guessed too many times and has lost 
    if len(missedLetters) == len(HANGMAN_PICS) - 1:
        displayBoard(missedLetters, correctLetters, secretWord)
        print('You have run out of guesses! \nAfter ' + str(len(missedLetters)) + 
    ' missed guesses and ' + str(len(correctLetters)) + 'correct guesses, the word was " '+ secretWord + '"')
        gameIsDone = True 

    #Ask the player if they want to play again (but only if the game is done)

    if gameIsDone:
        if playAgain():
            missedLetters = ''
            correctLetters = ''
            gameIsDone = False
            secretWord = getRandomWord(words)

        else:
           break










