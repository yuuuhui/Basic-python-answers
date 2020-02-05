c = eval(input("Enter an ASCII code:"))
if  c >= 0 and c <= 127:
    o = chr(c)
    print("The character is {}".format(o))
else:
    print("wrong input!")
