num = eval(input("Enter a three-digit integer:"))

if 99 < num < 1000:
    if str(num)[::-1] == str(num):
        print("{} is a palindrome".format(num))
    else:
        print("{} is not a palindrome".format(num))
    

else:
    print("The number is out of range!")
