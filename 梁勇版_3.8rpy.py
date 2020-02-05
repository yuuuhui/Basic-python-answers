#11.56 11
x = eval(input("Enter the amount:"))

tamount = x
currentd = int(x)
currentcent = (x - int(x)) * 100

print("The amount recorded is {} dollars {:.0f} cents".format(currentd,currentcent))
