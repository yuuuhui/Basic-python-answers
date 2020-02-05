print("i \t m(i)")
def m(i):
    sum = 0
    for x in range(1,i+1):
        sum += (x/(x+1))
        print("{:>2}".format(x),end = " \t")
        print("{:>7.4f}".format(sum))
        print("\n")
    


    


m(20)
        
