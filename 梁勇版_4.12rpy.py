num = eval(input("Enter an integer:"))


print("Is {} divisible by 5 and 6?".format(num))
print(num % 5 == 0 and num % 6 == 0)
    
print("Is {} divisible by 5 or 6? ".format(num))
print(num % 5 == 0 or num % 6 == 0)

print("Is {} divisible by 5 or 6, but not both?".format(num))
print(  (num % 5 == 0 or num % 6 == 0) and (not (num % 5 == 0 and num % 6 == 0) ) )

