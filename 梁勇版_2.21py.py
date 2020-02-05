ms = eval(input("Enter the monthly saving amount:"))
i = int(input("Enter the number of months:")) # 月数
rate = 1 + 0.00417
sum = 0 # 银行原先户头
for x in range(0, i ): # 月数
    sum = (sum + ms) * rate 
    print("After {}th month, the account value is {}".format(x + 1,sum))
    
