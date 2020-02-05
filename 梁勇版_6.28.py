import random


def x():
    iswin = True
    x = random.randint(1,6)
    y = random.randint(1,6)

    sum = x + y # 得出结果或者确定一个点


    print("You rolled {} + {} = {}".format(x,y,sum))


    if sum == 2 or sum == 3 or sum == 12:
        print("You lose!")
        iswin =False
    

    else:
        if sum == 7 or sum == 11:
            print("You win")
            iswin = True
        
        else:
    
            z = sum
            a = random.randint(1,6)
            b = random.randint(1,6)
            sum = a + b
            print("You rolled {} + {} = {}".format(a,b,sum))
    
            while sum != z and sum != 7:
                z = sum
                a = random.randint(1,6)
                b = random.randint(1,6)
                sum = a + b
                print("You rolled {} + {} = {}".format(a,b,sum))
            else:
                if sum == 7:
                
                    print("You lose")
                    iswin = False
                
                elif sum == z:
                
                    print("You win")
                    iswin = True
    return iswin

count = 0
for i in range(1000):
    if x() == True:
        count += 1
print(count)
                    
                
    
        
    
