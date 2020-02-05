import time
import random

start = str(input("Enter any key except \"end\" to continue :"))
if start != 'end':
    count = 0
    cn = 0
    st = time.time()
    while count < 5:
        x = random.randint(1,15)
        y = random.randint(1,15)
        sum = x + y
        ssstime = time.time()
        question = eval(input("Enter the answer to {} + {} :".format(x,y)))
        
        count += 1
        if question == sum:
            eeetime = time.time()
            tttime = eeetime - ssstime
            print("correct answer!time taken is {}".format(tttime))
            cn += 1
        else:
            eeetime = time.time()
            tttime = eeetime - ssstime
            print("wrong answer!time taken is {}".format(tttime))
           
    else:
        et = time.time()
        ttime = et - st
        print("The number of correct entry is {} ,\n the total time taken is {}".format(cn,ttime))

else:
    print("You have exited the app!")
