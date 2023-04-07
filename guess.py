# This is a Guess the Number Game
from operator import truediv
import random
guessesTaken = 0 # the player hasnt made any guesses yet so the value stored rn is 0

print('Hello! What is your name?')

name = input()
number = random.randint(1, 20)

print('Well, ' + name + 'I am thinking of a number between 1 and 20.' )

guessesTaken = 0
while guessesTaken < 6:

    print('Take a guess!')

    guess = input()

#if isinstance(guess, int) == False:
    # print('Not a valid input. Try Again')

    if not guess.isnumeric(): #checking if the guess if an integer 
        print('Please only input a number :(')
        continue

    guess = int(guess) # takes the argument "guess" and returns the argument as an integer. We basically need to convert our 
# string to an integer since we cannot compare the size of a string vs an integer

    if guess < number:
        print('Your guess is too low.')

    if guess > number:
        print('Your guess is too high.')


    if guess == number:
        break #break statement is only found in loops. We want to break out of the loop. 
#Goes to first line after the loop ending. 

    if guess == number:
        guessesTaken = str(guessesTaken + 1)
        print('Good Job ' + name + 'You guessed my number in ' + guessesTaken + ' guesses!')

    if guess != number:
        number = str(number)
        print('My number was ' + number)
