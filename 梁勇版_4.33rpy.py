num = eval(input("Enter a decimal value(0 - 15):"))



if 0 <= num <= 15:
    print("The hex value is {0:X}".format(num))
else:
    print("invalid input!")
    
