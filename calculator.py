import os

def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    return a/b

operations_dict={
    "+":add,
    "-":sub,
    "*":multiply,
    "/":divide
}

def calculator():

    num1=int(input("enter the first number: "))
    for sym in operations_dict:
        print(sym)
        
    conFlag=True
    while conFlag:
        
        symbol=input("pick an opportation from above: ")
        num2=int(input("enter the second number: "))

        calculateFunc=operations_dict[symbol]
        result=calculateFunc(num1,num2)
        print(f"Calculation answer is:{num1} {symbol} = {result}\n")

        wantContinue=input(f"enter 'y'- for continue with {result} OR 'n'- for new calculation OR 'e'- for exit").lower()
        
        if wantContinue=="y":
            num1=result
            
        elif wantContinue=="n":
            conFlag=False
            os.system('cls')
            calculator()
            
        else:
            conFlag=False
            print("Have a nice day byeee")

calculator()
    
    

