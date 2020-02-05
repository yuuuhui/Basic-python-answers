print("""
for ax + by =e
    cx + dy =f
""")
a,b,c,d,e,f = eval(input("Enter a,b,c,d,e,f: "))


h = a * d - b * c

if h == 0:
    print("The equation has no solution")
else:
    x = (e * d - b * f) /(a * d - b * c)
    y =  (a * f - e * c) / (a * d - b * c)
    print("x is {} and y is {}".format(x,y))


