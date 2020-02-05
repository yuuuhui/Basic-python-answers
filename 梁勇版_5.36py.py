from random import *
x = randint(1,3)
ans  = int(input("Enter (1,2,3)  to represent(scissor,stone,paper)"))


count = 0
countw = 0
countl = 0

while count != 2:

    if countw == 2:
        count  = countw
    elif countl == 2:
        count = countl

    elif x == 1:
        if ans == 1:
            print("The computer is scissor! You are scissors,too.Its a draw")
            

        elif ans == 2:
            print("The computer is scissor! You are stone.You have won the round!")
            countw += 1

        elif ans == 3:
            print("The computer is scissor! You are Paper.You have lost the round!")
            countl += 1
        if countw == 2 or countl == 2:
            pass
        else:
            x = randint(1,3)
            ans = int(input("Enter (1,2,3)  to represent(scissor,paper,stone)"))
            

    elif x == 2:
        if ans == 1:
            print("The computer is stone.You are scissor.You have lost the round!")
            countl += 1

        elif ans == 2:
            print("The computer is stone.You are stone too.Its a draw")
            

        elif ans == 3:
            print("The computer is stone.You are paper.You have won the round!")
            countw += 1
        if countw == 2 or countl == 2:
            pass
        else:
            
            x = randint(1,3)
            ans  = int(input("Enter (1,2,3)  to represent(scissor,paper,stone)"))

    elif x == 3:
        if ans == 1:
            print("The computer is paper.You are scissor.You have won the round!")
            countw += 1

        elif ans == 2:
            print("The computer is paper.You are stone.You have lost the round!")
            countl += 1

        elif ans == 3:
            print("The computer is paper.You are paper too.Its a draw")
        if countw == 2 or countl == 2:
            pass
        else:
            x = randint(1,3)
            ans  = int(input("Enter (1,2,3)  to represent(scissor,paper,stone)"))


else:
    if countw == 2:
        print("You have won the game!")
    elif countl == 2:
        print("You have lost the game!")
            


    

