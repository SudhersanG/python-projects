# Rock Paper Scizzer

import random





userch=input("'r' for rock\n 'p' for paper\n 's' for scizzers\n enter your choice:")
computer=random.choice(['r','p','s'])
print(f"computer choice is {computer}")


if(userch==computer):
  print("game is TIE:)")
  playercount=0
  opponentcount=0

elif((userch=='r' and computer=='p') or (userch=='p' and computer=='r') or (userch=='s' and computer=='p')):
      print("player won")

else:    
 print("opponent won")
      

     








