num1 = eval(input("Enter the 1st number:"))
num2 = eval(input("Enter the 2nd number:"))
num3 = eval(input("Enter the 3rd number:"))

if num1 > num2 > num3:
    print("{} < {} < {}".format(num3,num2,num1))
elif num1 > num3 > num2:
    print("{} < {} < {}".format(num2,num3,num1))
elif num2 > num3 > num1:
    print("{} < {} < {}".format(num1,num3,num2))
elif num2 > num1 > num3:
    print("{} < {} < {}".format(num3,num1,num2))
elif num3 > num1 > num2:
    print("{} < {} < {}".format(num2,num1,num3))
elif num3 > num2 > num1:
    print("{} < {} < {}".format(num1,num2,num3))
