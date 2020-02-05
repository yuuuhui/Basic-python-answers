



n = input("Please enter the bank acount to check the validity:")
try:
    n = int(n)
except ValueError:
    pass

while type(n) != int or n < 999999999999 or n > 10000000000000000000 :
    n = input("Please enter the bank acount to check the validity:")
    try:
        n = int(n)
    except ValueError:
        pass
    
else:
    pass


def findnoofdigit(n):
    count = 0
    i = n
    while i > 1:
        i /= 10
        count += 1
    return count
def checktype(n):
    z = findnoofdigit(n)
    check = n // (10 ** (z - 2)) 
    #print("check",check)
    if check == 37:
        print("The card type is American Express")
    else:
        check //= 10
        if check == 4:
            print("The card type is Visa")
        elif check == 5:
            print("The card type is Master")
        elif check == 6:
            print("The card type is Discover")
        else:
            print("error")

checktype(n)
sum1 = 0
sum2 = 0
y = findnoofdigit(n)
for x in range(1,y + 1):
    if x % 2 != 0:
        digit = n % 10
        twotimesdigit = digit * 2
        n //= 10
        #print(digit,end =" ")
        sum1 += digit
    if x % 2 == 0:
        digit = n % 10
        twotimesdigit = digit * 2
        n //= 10
        #print(digit,end =" ")
        sum2 += digit
#print(sum1,sum2)
sum = sum1 + sum2

if sum % 10 == 0:
    print("The card is valid")
else:
    print("The card is invalid")
    
