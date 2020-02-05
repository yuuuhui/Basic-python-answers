amount = eval(input("The amount invested:"))
annualr = eval(input("Annual interest rate:"))
monthlyr = annualr / 12
years = 30
def futureInvestmentValue(amount,monthlyr,years):
    print("Years \t Future value")
    for i in range(1,years+1):
        print("{:>2}".format(i),end = "\t ")
        print("{:<.2f}".format(amount * ((1 + monthlyr) ** (i * 12))))
        print("\n")

    
futureInvestmentValue(amount,monthlyr,years)
