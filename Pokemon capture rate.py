import math
import random 
#hp_max=input("Enter max hp of pokemon")
hp_max=100
#hp_current=input("Enter current hp of pokemon")
#hp_current=random.randint(0,100)
#while hp_current>hp_max:
#    hp_current=random.randint(0,100)
#print("Hp max",hp_max," Hp current",hp_current)
name=input("Enter the name of the pokemon")
hp_current=int(input("Enter the current health of the pokemon"))
hp_max=int(input("Enter the max health of the pokemon"))
rate=int(input("Enter caputure rate of pokemon"))
#rate=255
bonus_ball=int(input("Enter the multiplier you'd get for the ball used"))
#bonus_ball=1 #pokeball
bonus_status=int(input("Enter multiplier for any status effects"))
#bonus_status=1
a=((((3*hp_max)-(2*hp_current))*(rate*bonus_ball))/(3*hp_max))*bonus_status
print(a)
b=1048560/math.sqrt(math.sqrt(16711680/a))
print(b)
capture=False
counter=0
if a<=255:
    for i in range(4):
        x=random.randint(0,65535)
        print(x)
        if b <= x:
            print("fail")
            if counter==0:
                print("Oh, no! The Pokémon broke free!")
            elif counter==1:
                print("Aww! It appeared to be caught!")
            elif counter==2:
                print("Aargh! Almost had it!")
            elif counter==3:
                print("Shoot! It was so close, too!")
            break
        else:
            capture=True
            print("Sucessful")
            counter=counter+1
            if counter==4:
                print("Gotcha!",name," was caught!")
else:
    print("Gotcha!",name," was caught!")
