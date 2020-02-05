a,b,c = eval(input("Enter a,b,c:"))

r1 = (- b + (  (b ** 2) - 4 * a * c   ) ** 0.5) / (2 * a)
r2 = (- b - (  (b ** 2) - 4 * a * c   ) ** 0.5) / (2 * a)

x = b ** 2 - 4 * a * c
if x < 0:
    print("There is no real root")
elif x == 0:
    print("There is only one real root")
    print("The real root is {}".format(r1))


else:
    print("There are two real roots")
    print("The real roots are {} and {}".format(r1, r2))
