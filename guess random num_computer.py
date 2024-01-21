import random


print("                                ")
print("                                ")
print("WELCOME TO GUESS THE NUMBER GAME (.><.)")
print("---------------------------------------")
print("                                ")
print("                                ")                                  
    
 
def random_num(range):
    
    random_number=random.randint(1,range)
    guess=0

    
    while(guess!=random_number):
        guess=int(input("enter your guess number here :) :"))
        print("                                ")                  
        if(guess>random_number):
            print("oooopss...its too high bro :( ")
            print("                                ")                  
        elif(guess<random_number):
            print("ouch...its lowww bro :( ")
            print("                                ")                  
            

    if(guess==random_number):
        print(f"Wowwwww.....you got this {random_number}, you win")



random_num(10)
