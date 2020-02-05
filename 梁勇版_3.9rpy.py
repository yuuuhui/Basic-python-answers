n = str(input("Enter employee 's name:"))
h = eval(input("Enter number of hours worked in a week:"))
hpayrate = eval(input("Enter hourly pay rate:"))
ftwr = eval(input("Enter federal tax withholding rate: "))
stwr = eval(input("Enter state tax withholding rate: "))
workingdays = eval(input("Enter the number of working days:"))
grosspay = hpayrate * h
federalw = grosspay * ( ftwr )
statew = grosspay * (stwr )
totald = federalw + statew 
netp = grosspay - totald
print('''
Employee Name:{}
Hours worked: {}
Pay Rate: {}%
Gross Pay: ${}
Deduction:
    Federal Withholding({}%):$ {}
    State Withholding ({}%):$ {}
    Total Deduction: $ {}
Net Pay: ${}
'''.format(n,h,hpayrate ,grosspay,ftwr,federalw,stwr,statew,totald,netp))
