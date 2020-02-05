'''
0 - 剪刀
1 - 石头
2 - 布
2 > 1 > 0 > 2 

'''
import random

num = random.randint(0,2)
ans = eval(input("scissor(0) ,rock(1),paper(2):"))


if ans == num:
    if ans == 0:
        print("The computer is scissor.You are scissor,too.It's a draw. ")
    
    if ans == 1:
        print("The computer is stone.You are stone,too.It's a draw. ")
    if ans == 2:
        print("The computer is paper.You are paper,too.It's a draw. ")
elif ans == 0:
    if num == 1:
        print("The computer is stone.You are scissor.You lost.")
    if num == 2:
        print("The computer is paper.You are scissor.You won.")
elif ans == 1:
    if num == 0:
        print("The computer is scissor.You are stone.You won.")
    if num == 2:
        print("The computer is paper.You are stone.You lost.")

elif ans == 2:
    if num == 0:
        print("The computer is scissor.You are paper.You lost.")
    if num == 1:
        print("The computer is stone.You are paper.You won.")
else:
    print("Wrong input!")
    



    

