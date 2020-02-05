import random

#输入数字与股票完全符合
num = random.randint(100,999)
print(num)

ans = eval(input("Enter a number between 100 and 999:"))


#digit from actual:
digit1 = num % 10
digit100 = num // 100
digit10 = num - digit1 -(num // 100 * 100)

#digit from guess
gdigit1 = ans % 10
gdigit100 = ans //100
gdigit10 = ans - gdigit1 - (ans // 100 * 100)





if num > 100 or num < 999:
    if num == ans:
        print("perfect match: you win the 10000 dollars prize")
    elif digit1 == gdigit1 \
            or digit1 == gdigit10 \
            or digit10 == gdigit100 \
            and digit10 == gdigit1 \
            or digit10 ==gdigit10 \
            or digit10 == gdigit100  \
            and digit100 == gdigit1 \
            or digit100 == gdigit10 \
            or digit100 == gdigit100: 
                print("all digits match: you win 3000 dollars prize ")
    elif digit1 == gdigit1 \
            or digit1 == gdigit10 \
            or digit1 == gdigit100 \
            or digit10 == gdigit1\
            or digit10 == gdigit10\
            or digit10 ==gdigit100\
            or digit100 == gdigit1\
            or digit100 == gdigit10\
            or digit100 == gdigit100:
                print("Match one digit: you win 1000 dollars prize")
    else:
        print("Try next time.Good luck!")


else:
    print("wrong input!")

