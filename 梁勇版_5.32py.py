amount  =eval(input("Enter an amount;"))
rate = eval(input("Enter the annual interest rate in x %(Enter x):"))
month = int(input("Enter the number of months:"))

sum = 0
for i in range(1,month):
    sum += amount * (  (1 + rate/1200) ** (i))
    print("{:.3f}".format(sum))
    
