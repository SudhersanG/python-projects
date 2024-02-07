import random
import GuessTheNumberLogo
def easyLevel():
    flag=10
    for i in range(flag):
        userGuess=int(input("tell you guess now: "))
                      
        if userGuess == compNum:
            print("Wowww...you Guessed the number and YOU WIN!")
            break
       
        elif userGuess != compNum:
            flag=flag-1
            print(f"oooops...you have only {flag} attempts balance to play")

            if userGuess > compNum:
                print("your guess is high")

            if userGuess < compNum:
                print("your guess is low")

            if flag == 0:
                print("you lose")
                break

def mediumLevel():
    flag=5
    for i in range(flag):
        userGuess=int(input("tell you guess now: "))
                      
        if userGuess == compNum:
            print("Wowww...you Guessed the number and YOU WIN!")
            break
       
        elif userGuess != compNum:
            flag=flag-1
            print(f"oooops...you have only {flag} attempts balance to play")

            if userGuess > compNum:
                print("your guess is high")

            if userGuess < compNum:
                print("your guess is low")

            if flag == 0:
                print("you lose")
                break

def hardLevel():
    flag=3
    for i in range(flag):
        userGuess=int(input("tell you guess now: "))
                      
        if userGuess == compNum:
            print("Wowww...you Guessed the number and YOU WIN!")
            break
       
        elif userGuess != compNum:
            flag=flag-1
            print(f"oooops...you have only {flag} attempts balance to play")

            if userGuess > compNum:
                print("your guess is high")

            if userGuess < compNum:
                print("your guess is low")

            if flag == 0:
                print("you lose")
                break

print(GuessTheNumberLogo.logo)
endGame=True
while endGame:
   
    
    print("Guess a Number between 1-50 ")
    print("Let me a think a number:")
    compNum=random.randint(1,50)
    print("choose your difficulty level attempts: easy-10/medium-5/hard-3")
    diffLevel=input("Now Enter the level: ").lower()

    if diffLevel=="easy":
        easyLevel()
        
    elif diffLevel=="medium":
        mediumLevel()

    elif diffLevel=="hard":
        hardLevel()

    play=input("you want to play again? yes/no ").lower()
    if play=="yes":
        endGame=True
    else:
        endGame=False


