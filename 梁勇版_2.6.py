#999 (999 //10 = 99  99 % 10 
number = eval(input("Enter a number between 0 and 1000:"))
sum = number % 10 + ( (number // 10) % 10) + (number // 100)   
#个位数 十位数 百位数
print(sum)
