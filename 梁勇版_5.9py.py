a = 10000
currentyear = 1
sum = 0 
while currentyear <5:
    
    a *= ((1.05) **(currentyear - 1))
    sum += a
    print("the amout of year {} is {:.2f} .total amount paid is {:.2f}".format(currentyear,a,sum))
    currentyear += 1
       
