import random
lst =["snake","water","gun"]
i=0
com_won=0
u_won=0
print("!!!!!!!!!!! _______Welcome to the this awesome game named snake_water_gun______!!!!!!!!!!!")
player_name=str(input("please enter your name: "))
n=int(input(F"dear {player_name} how many times do you want to paly the game: "))
while i<n:
    a = random.choice(lst)
    b = str(input("enter your choice snake/water/gun: "))
    if a=="snake":
        if b=="water":
            print("computer won!!! ")
            com_won+=1
        elif b=="gun":
            print("You won!!!  ")
            u_won+=1
        elif b=="snake":
            print("tied!!!   ")
        else:
            print(F"dear {player_name} have enters the wrong input",end="please enter the valid option :snake/gun/water: ")
    elif a=="water":
        if b=="gun":
            print("computer won!!! ")
            com_won+=1
        elif b=="snake":
            print("You won!!!  ")
            u_won+=1
        elif b=="water":
            print("tied!!!   ")
        else:
            print(F"dear {player_name} have enters the wrong input",end="please enter the valid option :snake/gun/water: ")
    else:
        if b=="water":
            print("computer won!!! ")
            com_won+=1
        elif b=="snake":
            print("You won!!!  ")
            u_won+=1
        elif b=="gun":
            print("tied!!!")
        else:
            print(F"dear {player_name} have enters the wrong input",end="please enter the valid option :snake/gun/water: ")
    i+=1
print("\ncomputer won: ",com_won)
print("\nyou won: ",u_won)
if com_won>u_won:
    print("\ncomputer won the game!!!")
elif com_won<u_won:
    print("\nyou have won the game!!")
else:
    print("\nmatch tied")