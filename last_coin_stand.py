import random as rand
import time as t
coin=20
turn=1
while coin:
    if turn==1:
        take=int(input("enter the coin from it "))
        while take not in [1,2,3] or take>coin:
            print(".....player choice......\n")
            take=int(input("invalid input \n please enter a new one "))
        print(f"player {take} from the coin box ") 
    else:
        take=rand.randint(1,min(3,coin))
        print(".....bot's choice....")
        t.sleep(2)
        print("bot is thinking ....")
        t.sleep(3)
        print(f"bot {take} from the coin box ")
    coin=coin-take     
    turn=1-turn
    print(f"remain coins {coin}")
if turn is not 1:
    print("Congratulations player you wins the game ")    
else:
    print("bot wins the game ") 
