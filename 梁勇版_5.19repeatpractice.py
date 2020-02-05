
n = int(input("Enter the number of lines:"))




for i in range(1,n):#i is the current line
    print("  " * ( n - i),end = " ")
    y = i
    for k in range(i,0,-1):
        print(i,end = " ")
        i -= 1
    for x in range(2,y + 1):
        print(x,end = " ")
           
    print("\n")
