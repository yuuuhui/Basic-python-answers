loan = eval(input("Loan Amount"))
year = int(input("Number of Years:"))
rate = eval(input("Annual Interest Rate:"))
monthly = (loan * rate / 12) / (1 - 1 / ((1 + rate / 12) ** (year * 12)))
total = monthly * 12 * year
print("Monthly Payment:{:.2f}".format(monthly))
print("Total Payment:{:.2f}".format(total))

print("Payment# \t Interest \t Principal \t Balance")
count = 1

while count <= 12:
    
    interest = loan * (rate / 12)
    principal = monthly - interest
    loan -= principal
    print(count, "\t","\t","{:.2f}".format(interest), "\t\t","{:.2f}".format(principal),"\t","{:.2f}".format(loan))
    count += 1
