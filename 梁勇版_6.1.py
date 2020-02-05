

def getPentagonalNumber(n):
    print("{:.0f}".format(n * (3 * n - 1) / 2),end = " ")

for i in range(100):
    getPentagonalNumber(i)
    
