print("LOVE CALCULATOR")
print("---------------")


your_name=input("enter your name:")
her_name=input("enter her name:")

name=(your_name + her_name).lower()
t=int(name.count('t'))
r=int(name.count('r'))
u=int(name.count('u'))
e=int(name.count('e'))

true=t+r+u+e

l=int(name.count('l'))
o=int(name.count('o'))
v=int(name.count('v'))
e=int(name.count('e'))

love=l+o+v+e

loveScore=int(str(true)+str(love))

if loveScore>=80:
    print("amazing couplezzzzzz :)")
elif loveScore<80 and loveScore>=50:
    print("good couplezzzzzz :)")
elif loveScore<50 and loveScore>=20:
    print("Normal coupleeezzzzzz:)")
elif loveScore<20:
    
    print("You both will breakup soonn :(")
