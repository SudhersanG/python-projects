import random
import hangmanStages

words=['hang','man','hangman','book','note','pencil','phone','chair','python','skydive']
choosedWord=random.choice(words)

print(choosedWord) #hang

display=[]

for i in range(0,len(choosedWord)):
    display+='-'
    
print(display) #['-','-','-','-']


lives=6

while lives!=0:
    guessLetter=input("enter your guesss letter:").lower() #h
    for index in range(len(choosedWord)):#0 1 2 3
        letter=choosedWord[index]#h
        if letter==guessLetter:
            display[index]=letter
            
    print(display)
    
    if guessLetter not in choosedWord:
        lives-=1
        print(f"you have only {lives} lives")

    if lives==0:
        print("you lose")

    if "-" not in display:
        print("you win")
        break
    
    print(hangmanStages.hangman_stages[lives])
