num1,num2,num3 = eval(input("Enter three numbers as x,y,z:"))
def sort(num1,num2,num3):
    if num1 <= num2 and num1 <= num3:
        print(num1,end = " ")
        if num2 <= num3:
            print(num2,end = " ")
            print(num3,end = " ")
        elif num3 < num2:
            print(num3,end = " ")
            print(num2,end =" ")
    elif num2 <= num1 and num2 <= num3:
        print(num2,end = " ")
        if num1 <= num3:
            print(num1,end =" ")
            print(num3,end =" ")
        elif num3 < num1:
            print(num3,end =" ")
            print(num1,end =" ")
    elif num3 <= num1 and num3 <= num2:
        print(num3,end = " ")
        if num1<= num2:
            print(num1,end = " ")
            print(num2,end = " ")
        elif num2< num3:
            print(num2,end = " ")
            print(num1,end = " ")
    elif num1 == num2 == num3:
        print(num1,num2,num3)
    
    
        

sort(num1,num2,num3)
