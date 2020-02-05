n = eval(input("Enter an integer: "))
# number of spaces
maxspace = 2 * (n -1)



for  i in range(1,n+1):
    x = i
    currentspace = n - i
    print(currentspace * "  ",end = " ")
    for k in range(i,0,-1):
        print(i,end = " ")
        i-=1
    
    for g in range(2,x+1):
        print(g,end =" ")
        
        
            
        
    print("\n")
        
  
