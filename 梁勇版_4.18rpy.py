exr = eval(input("Enter the exchange rate from dollars to RMB:"))
currency = eval(input("Enter 0 to convert dollars to RMB and 1 vice versa"))


if currency == 0:
    damount = eval(input("Enter the dollar amount"))
    ramount = exr * damount
    print("${} is {} yuan".format(damount,ramount))
elif currency == 1:
    ramount = eval(input("Enter the RMB ampunt:"))
    damount = ramount / exr
    print("{} yuan is ${}".format(ramount,damount))
else:
    print("Incorrect input!")




