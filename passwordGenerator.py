import random
smallLetters=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
capLetters=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
nums=['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols=['!', '@', '#', '$', '%', '^', '&', '*']

print("------------------------------")
print("....MAH PASSWORD GENERATOR....")
print("------------------------------")
password=""
smalLetCount=int(input("enter how many smallLetters you want:"))
for i in range(1,smalLetCount+1):
    char=random.choice(smallLetters)
    password+=char
#print("pasword is:",password)

capLetCount=int(input("enter how many capLetters you want:"))
for i in range(1,capLetCount+1):
    char=random.choice(capLetters)
    password+=char
#print("pasword is:",password)

numCount=int(input("enter how many nums you want:"))
for i in range(1,numCount+1):
    char=random.choice(nums)
    password+=char
#print("pasword is:",password)

symCount=int(input("enter how many symbols you want:"))
for i in range(1,symCount+1):
    char=random.choice(symbols)
    password+=char
print("your normal pasword here:",password)
print()

strongPassword=list(password)
random.shuffle(strongPassword)
newstrongPassword=""
passlen=len(strongPassword)
for i in range(0,passlen-1):
    newstrongPassword+=strongPassword[i]
print("Your Strong password here:",newstrongPassword)




