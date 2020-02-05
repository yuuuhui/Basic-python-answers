amount= eval(input("Enter the initial deposit amount:"))
percentage = eval(input("Enter the annual percenrage yield:"))
period = eval(input("Enter maturity period (number of months):"))



sum = 0
print("Month \t CD Value")
for i in range(1,period+1):
     amount *= (1 + percentage/1200) 
     print("{:>2}".format(i),"\t","{:.2f}".format(amount))
