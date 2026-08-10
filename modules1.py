
# #random module
# # import random
# # print(random.randint(1,10))


# # fruits=["apple","orange","pineapple","grapes","mango","watermelon"]
# # print(random.choice(fruits))

# # #coin toss
# # ch=("heads","tails")
# # print(random.choice(ch))
# # z=random.randint(0,1)
# # if z:
# #     print("heads")
# # else:
# #     print("tails")    


# #rock paper scissor
# import random
# ch=("rock","paper","scissor")
# comp=random.choice(ch)
# player=""
# while player not in ch:
#     player=input("enter your choice rock/paper/scissor:---")
# print(f"player:- {player}\ncomputer:-{comp}")
# if player==comp:
#     print("its a tieee")
# elif comp=="rock":
#     if player=="scissor":
#         print("rock smashes scissor computer wins")
#     else:
#         print("paper covers rock player wins")
# elif comp=="paper":
#     if player=="rock":
#        print("paper covers rock computer wins")
#     else:
#         print("rock beats scissor player wins")   
# elif comp=="scissor":
#     if player=="paper":
#         print("scissor cut the paper player wins")
#     else:
#         print("rock beats scissor comp wins")        


# #create an rpg game
# import random
# player=100
# eneymy=100
# while player>0 and eneymy>0:
#     print("player health:-",player)
#     print("enemy health:-",eneymy)
#     print("1. attack")
#     print("2. heal")
#     choice = input("enter your choice:-")
#     if choice=="1":
#         damage=random.randint(10,20)
#         eneymy-=damage
#         print(f"you attacked the enemy and dealt {damage} damage")
#     elif choice=="2":
#         heal=random.randint(10,20)
#         player+=heal
#         print(f"you healed yourself for {heal} health")
#     else:
#         print("invalid choice")
    
#     if eneymy>0:
#         enemy_damage=random.randint(5,15)
#         player-=enemy_damage
#         print(f"enemy attacked you and dealt {enemy_damage} damage")

import random
player=input("enter your name:---").lower()
enemy=random.choice(["dragon","gobin","troll"])
playerhp=100
eneymyhp=100
turn=1
while playerhp>0 and eneymyhp>0:
    print(f"Turn{turn}")
    print(f"{enemy}attacks player")
    playerhp=playerhp-random.randint(8,20)
    print(F"PLAYER HP{playerhp}")
    print(F"{player} strikes back")
    eneymyhp=eneymyhp-random.randint(8,20)
    print(f"eneymy hp{eneymyhp}")
    turn=turn+1
    if playerhp <=0:
        print(f"{enemy}won")
        break
    elif eneymyhp <=0:
        print(f"{playerhp}won")
        break
