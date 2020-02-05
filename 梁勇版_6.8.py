
 

def celsiusToFahrenheit(celcius):
    fahrenheit = (9/5) * celcius + 32
    print("{:.1f}".format(fahrenheit),end = "\t\t ")

def FahrenheitToCelcius(fahrenheit):
    celcius = (5/9) * (fahrenheit - 32)
    print("{:.1f}".format(celcius),end = "\t ")


print("Celcius \t Fahrenheit \t Fahrenheit \t Celcius")
k = 120
for i in range(40,30,-1):
    print("{:.1f}".format(i), end = "\t\t  ")
    celsiusToFahrenheit(i)
    print("{:.1f}".format(k),end = "\t\t ")
    
    FahrenheitToCelcius(k)
    k -= 10
    
          
    print("\n")

    

