# This a guess the number game.


import random

#decor time:
print('Hello! what is your name?')
name=input()

print('Hello! '+name+ '. My name is Jarvis.\nWell, '+name +'. I am thinking of a number between 1 and 20')
secretNumber=random.randint(1,20)

for guessesTaken in range(1,7):
    print('Take a guess.')
    #guess=int(input())

#### Why this conditioning is importtant? ####
#     Because it will only improve our guesses
    try:
        guess=int(input())   #### but how? - stackoverflow
        if guess < secretNumber:
             print('Too Low')
        elif guess > secretNumber:
             print('Too high')
        else:
             break        #This is for the correct guess
    except:
        print('That is not a number')

if guess == secretNumber:
    print('Good Game. '+'You guessed it correctly in '+ str(guessesTaken)+' guesses')
else:
     print('Nope. The number I was thinking of was '+str(secretNumber)) 
      
      