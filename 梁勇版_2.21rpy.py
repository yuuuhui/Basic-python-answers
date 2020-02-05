ms = eval(input("Enter the monthly saving amount:"))
r = 0.00417
x = 6
av = ms * (1 - (1 + r) ** (6 + 1)) / (1 - (1 + r)) - ms
print("After the sixth month, the account value is {}".format(av))
