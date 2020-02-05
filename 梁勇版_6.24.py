


    

def isprime():
    count = 0
    i = 0
    n = 1000
    
    while i < n:
        
        divisor = 2
        isprimenumber = True
        
        while divisor < i  :
            if i % divisor == 0:
                isprimenumber = False
                break
            else:
                pass
            divisor += 1
        i += 1
        
        
    
        if isprimenumber == True and str(i)[::-1] == str(i):
            print(i,end = "\t" )
            count += 1
            if count % 10 == 0:
                print("\n")
        while count >= 100:
            break
        else:
            n += 1
               

isprime()
        
        



            
            
            
