a = eval(input("Enter an integer:")) # 输入数字
numbers = []       #create a list
for i in str(a): 
    numbers.append(i) # 把数学加入一个list
    
numbers.reverse() #把numbers反过来

finalnumber = str()
for x in numbers:
   finalnumber += x
b = int(finalnumber)


print(b + 1)






