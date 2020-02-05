print(" \t Multiplication table")
print("\n")

print("     1   2   3   4   5   6   7   8   9 ")
print("  ---------------------------------------")
for i in range(1,10):
    print(i,"|",end = " ")
    for k in range(1,10):
        print("{:>2}".format(i * k),end = "  ")
    print("\n")
    
