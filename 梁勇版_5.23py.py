loan = eval(input("Loan Amount:"))
year = eval(input("Number of years:"))

print("Interest Rate \t Monthly Payment \t Total Payment")

rate = 0.0500

while rate <= 0.0800:
    monthly = (loan * rate / 12) / (1 - 1 / ((1 + rate / 12) ** (year * 12)))
    total = monthly * 5 * 12
    print("{:.3f} %".format(rate * 100),"\t","{:.2f}".format(monthly),"\t","\t","{:.2f}".format(total))
    rate += (0.00125)
                
