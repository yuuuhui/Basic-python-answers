
print("i \t m(i)")

def m(i):
    sum = 0
    y = 0
    for x in range(1,i+1):
        y += (((-1) ** (x + 1)) / ((2 * x) - 1))
        sum = y * 4
            
        if (x - 1) % 100 == 0:
            print(x,end = "\t")
            print("{:.4f}".format(sum))
        else:
            pass
            
    
        
   
m(201)  

