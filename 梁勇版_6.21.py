
n = int(input("Enter the value of n:"))

def sqrt(n):
    
    for lastguess in range(1,n):
        nextguess = (lastguess + (n / lastguess)) / 2
        if abs(nextguess - lastguess) < 0.0001:
            print(nextguess)
            break
    
sqrt(n)
