w1,p1 = eval(input("Enter weight and price for package 1:"))
w2,p2 = eval(input("Enter weight and price for package 2:"))

a1 = w1 / p1
a2 = w2 / p2

if a1 > a2:
    print("Package 1 has the better price.")
elif a1 == a2:
    print("Package 2 and package 1 have the same price")
else:
    print("Package 2 has the better price.")
