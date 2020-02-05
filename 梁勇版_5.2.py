import time
import random
start = str(input("Enter anythong to start,\n enter 'end' to stop the quiz:"))
cn = 0
while start != "end":
    x = random.randint(1,15)
    y = random.randint(1,15)
    sum = x + y
    st = time.time()
    ans = eval(input("please enter the answer to the question {} + {}:".format( x,y)))
    if ans == sum:
        cn += 1
        et = time.time()
        time = et - st
        print("correct answer!the number of correct input is {} total time taken is {}".format(cn,time))
    else:
        print("wrong answer!the number of correct input is {} ".format(cn) )
        et = time.time()
        time = et - st

else:
    print("You have exit the app!")



