from random import *
n = int(input("Enter n for n * n matrix:"))
def printMatrix(n):
    for i in range(n):
        count = 0
        for k in range(n):
            count += 1
            x = randint(0,1)
            print(x,end = " ")
            if count % n == 0:
                print("\n")
        
        

printMatrix(n)
