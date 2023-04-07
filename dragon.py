import random #provides the randint function
import time  #has time related functions

def displayIntro ():
    print(''' You are in a land full of monsters, such as dragons or goblins. 
    In front of you, you see two caves.
    In one cave, 
    there is a friendly dragon with lots of treasure. 
    This dragon is nice and will share with you. In the other, there is a greedy
    dragon who will eat you on sight.''')
    print()

def chooseCave():
    cave = '' #stores a blank string 
    while cave != '1' and cave != '2': #input validation, connected by boolean "and". This statement is true since the blank string has no value.
        print('Which cave will you go into?')
        cave = input() #if the player entered 1 or 2 then the cave will be either 1 or 2. This makes the while condiiton false and the program will go
        # past the while loop. If you entered hello or smth then the while loop would go again. This makes sure the player enters 1 or 2. 
        
        return cave #the def block ends here

 
def checkCave(chosenCave):
    print('You approach the cave...')
    time.sleep(2) #pauses the program for 2 seconds 
    print('It is dark and spooky...')
    time.sleep(2)
    print('A large dragon jumps outs in front of you! He opens his jaws and...')
    print()
    time.sleep(2)

    friendlyCave = random.randint(1,2)

    if chosenCave == str(friendlyCave): #chosenCave is a string since we had '1' and '2' and friendly cave is a integer bcuz of randint. So we need to convert friendlyCave to a string.
        print("Gives you his treasure!")

    else:
        print('Gobbles you down in one bite heheheheheh')

playAgain = 'yes'
while playAgain == 'yes' or playAgain == 'y':
    displayIntro()
    caveNumber = chooseCave()
    checkCave(caveNumber)
    
    print('Do you want to play again? (yes or no)')
    playAgain = input()