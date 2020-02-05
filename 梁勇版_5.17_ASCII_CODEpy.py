#33-126 ! - ~
count = 0
n =33
while n < 127:
    print(chr(n),end = "")
    n += 1
    count += 1
    if count % 10 ==0:
        print("\n")
    else:
        continue
else:
    pass
    
