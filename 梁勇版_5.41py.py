num = int(input("Enter a number(0:for end of input!):"))
count = 0

numlist = []
while num != 0:
    num = int(input("Enter a number(0:for end of input!):"))
    numlist.append(num)
    if num == max(numlist):
        count += 1
        

else:
    print("The largest number is",max(numlist))
    print("The occurence count of the largest number is {} ".format(count))

