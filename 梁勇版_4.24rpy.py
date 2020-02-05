ace = "Ace"

eleven = "Jack"
twelve = "Queen"
thirteen = "King"

c1 = "spades"
c2 = "Heart"
c3 = "diamonds"
c4 = "clubs"


import random

num = random.randint(1,14)
color = random.randint(1,4)
gsize = random.randint(0,1)

if num == 14:
    if gsize == 0:
        print("The card you picked is red King")
    if gsize == 1:
        print("The card you picked is black King")
    else:
        print("Error occured")
else:
    if color ==  1:
        if num == 1:
            print("The card you picked is {} of {}".format(ace,c1))
        elif num == 2:
            print("The card you picked is {} of {}".format(num,c1))
        elif num == 3:
            print("The card you picked is {} of {}".format(num,c1))
        elif num == 4:
            print("The card you picked is {} of {}".format(num,c1))
        elif num == 5:
            print("The card you picked is {} of {}".format(num,c1))    
        elif num == 6:
            print("The card you picked is {} of {}".format(num,c1))
        elif num == 7:
            print("The card you picked is {} of {}".format(num,c1))
        elif num == 8:
            print("The card you picked is {} of {}".format(num,c1))
        elif num == 9:
            print("The card you picked is {} of {}".format(num,c1))
        elif num == 10:
            print("The card you picked is {} of {}".format(num,c1))
        elif num == 11:
            print("The card you picked is {} of {}".format(eleven,c1))
        elif num == 12:
            print("The card you picked is {} of {}".format(twelve,c1))
        elif num == 13:
            print("The card you picked is {} of {}".format(thirteen,c1))
                  
    elif color == 2:
        if num == 1:
            print("The card you picked is {} of {}".format(ace,c2))
        elif num == 2:
            print("The card you picked is {} of {}".format(num,c2))
        elif num == 3:
            print("The card you picked is {} of {}".format(num,c2))
        elif num == 4:
            print("The card you picked is {} of {}".format(num,c2))
        elif num == 5:
            print("The card you picked is {} of {}".format(num,c2))   
        elif num == 6:
            print("The card you picked is {} of {}".format(num,c2))
        elif num == 7:
            print("The card you picked is {} of {}".format(num,c2))
        elif num == 8:
            print("The card you picked is {} of {}".format(num,c2))
        elif num == 9:
            print("The card you picked is {} of {}".format(num,c2))
        elif num == 10:
            print("The card you picked is {} of {}".format(num,c2))
        elif num == 11:
            print("The card you picked is {} of {}".format(eleven,c2))
        elif num == 12:
            print("The card you picked is {} of {}".format(twelve,c2))
        elif num == 13:
            print("The card you picked is {} of {}".format(thirteen,c2))

        
    elif color == 3:
        if num == 1:
            print("The card you picked is {} of {}".format(ace,c3))
        elif num == 2:
            print("The card you picked is {} of {}".format(num,c3))
        elif num == 3:
            print("The card you picked is {} of {}".format(num,c3))
        elif num == 4:
            print("The card you picked is {} of {}".format(num,c3))
        elif num == 5:
            print("The card you picked is {} of {}".format(num,c3))   
        elif num == 6:
            print("The card you picked is {} of {}".format(num,c3))
        elif num == 7:
            print("The card you picked is {} of {}".format(num,c3))
        elif num == 8:
            print("The card you picked is {} of {}".format(num,c3))
        elif num == 9:
            print("The card you picked is {} of {}".format(num,c3))
        elif num == 10:
            print("The card you picked is {} of {}".format(num,c3))
        elif num == 11:
            print("The card you picked is {} of {}".format(eleven,c3))
        elif num == 12:
            print("The card you picked is {} of {}".format(twelve,c3))
        elif num == 13:
            print("The card you picked is {} of {}".format(thirteen,c3))
    elif color == 4:
        if num == 1:
            print("The card you picked is {} of {}".format(ace,c4))
        elif num == 2:
            print("The card you picked is {} of {}".format(num,c4))
        elif num == 3:
            print("The card you picked is {} of {}".format(num,c4))
        elif num == 4:
            print("The card you picked is {} of {}".format(num,c4))
        elif num == 5:
            print("The card you picked is {} of {}".format(num,c4))   
        elif num == 6:
            print("The card you picked is {} of {}".format(num,c4))
        elif num == 7:
            print("The card you picked is {} of {}".format(num,c4))
        elif num == 8:
            print("The card you picked is {} of {}".format(num,c4))
        elif num == 9:
            print("The card you picked is {} of {}".format(num,c4))
        elif num == 10:
            print("The card you picked is {} of {}".format(num,c4))
        elif num == 11:
            print("The card you picked is {} of {}".format(eleven,c4))
        elif num == 12:
            print("The card you picked is {} of {}".format(twelve,c4))
        elif num == 13:
            print("The card you picked is {} of {}".format(thirteen,c4))





    
