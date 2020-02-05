#mode c

for i in range(1,7):
    print((6 - i) * "  ",end = " ")
    for k in range(i,0,-1):
        print(k,end = " ")
    print("\n")
