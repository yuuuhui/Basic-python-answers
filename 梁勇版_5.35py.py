

for i in range(1,10001):
    sum = 0
    
    for k in range(1,i):
        if i % k == 0:
            sum += k
        else:
            continue
        

    if sum != i:
        continue
    else:
        print(i)
        
    
