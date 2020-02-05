a,b,c = eval(input("Enter three edges:"))
p =a + b + c


if a + b > c and abs(a - b) < c\
   and a + c > b and  abs(a - c) < b\
   and b + c > a and  abs(b - c) < a:
    print("The perimeter is {}".format(p))
else:
    print("The input is invalid!")
