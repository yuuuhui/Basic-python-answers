
n = int(input("Enter the number n:"))
def displayPattern(n):
    for i in range(1,n + 1):
        print("  " * (n - i),end = " ")
        for k in range(i,0,-1):
            print(k,end  = " ")
        print("\n")
        
    
    
displayPattern(n)
