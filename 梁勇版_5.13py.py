#被5 或 6 整除 但是不被他们同时整除的数
for i in range(100,1000):
    if i % 5 == 0 and i % 6 == 0:
        continue
    elif i % 5 == 0 or i % 6 == 0:
        print(i,end = " ")
    else:
        continue
