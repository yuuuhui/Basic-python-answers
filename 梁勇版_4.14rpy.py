#0代表head 1 代表tail

import random
a = random.randint(0,1)
ans = eval(input("Enter your answer(0 - head , 1 - tail):"))

if ans == 0 or ans == 1:
    if ans == a:
        print("the answer is {} and you are correct!".format(a))
    else:
        print("the answer is {} and your answer is  wrong!".format(a))
        
    

else:
    print("wrong input")








