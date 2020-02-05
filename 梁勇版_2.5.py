subtotal,rate= eval(input("Enter the subtotal and a gratuity rate:"))
gratuity = subtotal * (rate / 100) 
total = subtotal + gratuity
print("the gratuity is {} and total is {}".format(gratuity,total))
