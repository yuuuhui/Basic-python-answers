
#numberOfPrimes = 50
numberOfPrimesPerLine = 8
count = 0

        
print("The prime numbers between 2 and 1000 are:")

for numberOfPrimes in range(2, 1000):

    isPrime = True

    divisor = 2

    while divisor <= numberOfPrimes / 2:
        if numberOfPrimes % divisor == 0:

            isPrime = False
            break
        divisor += 1

    if isPrime:
        count += 1

        print(numberOfPrimes, end= " ")

        if count % numberOfPrimesPerLine == 0:

            print('\r')

    
