menu={
    "latte":{
        "ingredients":{
            "water":200,
            "milk":100,
            "coffee":25
         },
        "cost":150
    },
    "espresso":{
        "ingredients":{
            "water":50,
            "coffee":18
         },
        "cost":100
    },
    "cappuccino":{
        "ingredients":{
            "water":250,
            "milk":100,
            "coffee":24
         },
        "cost":200
    }
}


def makeCoffee(coffeeName,coffeeIngredients):
    for item in coffeeIngredients:
        resources[item]-=coffeeIngredients[item]
    print(f"here is your {coffeeName}....have it and Enjoy :) ")      



def isPaymentSuccessful(moneyReceived,coffeeCost):
    if moneyReceived>=coffeeCost:
        global profit
        profit+=coffeeCost
        change=moneyReceived-coffeeCost
        print(f"Here is your change Rs.{change}")
        return True
    else:
        print(f"Sorry this Rs.{moneyReceived}is not enough. Money refunded.")
        return False
    

def checkResources(orderIncredients):
    for item in orderIncredients:
        if orderIncredients[item]>resources[item]:
            return False
    return True


def processCoins():
    print("Please insert coins for coffee")
    total=0
    coinFive=int(input("how many 5rs coin?: "))
    coinTen=int(input("how many 10rs coin?: "))
    coinTwenty=int(input("how many 20rs coin?: ")) 
    total=(coinFive*5)+(coinTen*10)+(coinTwenty*20)
    print(f"total is {total}")
    return total

        
profit=0

resources={
    "water":500,
    "milk":200,
    "coffee":100,
}


isOn=True
while isOn:
    choice=input("what would you like to prefer?(latte/espresso/cappuccino):").lower()
    if choice=="off":
        isOn=False

    elif choice=="report":
        print(f"water={resources['water']}.ml")
        print(f"milk={resources['milk']}.ml")
        print(f"coffee={resources['coffee']}.g")
        print(f"money={profit}")

    else:
        coffeeType=menu[choice]
        print(coffeeType)

        if checkResources(coffeeType['ingredients']):
            payment=processCoins()
            
            if isPaymentSuccessful(payment,coffeeType['cost']):
                makeCoffee(choice,coffeeType['ingredients'])



print("Thank you for your visiting...Have a nice day...")






















    
