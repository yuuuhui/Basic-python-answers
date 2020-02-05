bsalary = 5000

monextra = 30000 / 12 - 5000/12
rate1 = 0.08
rate2 = 0.10
rate3 = 0.12


#case 1

if monextra / 0.08 < 5000:
    sale = monextra / rate1
    print(sale)
elif monextra / 0.10 <10000:
    sale = monextra / rate2 
    print(sale)
else:
    sale = monextra / rate3
    print(sale)





