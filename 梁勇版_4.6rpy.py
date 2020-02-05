w = eval(input("Enter weigght in pounds:"))
feet = eval(input("Enter feet:"))
inch = eval(input("Enter inches:"))
height = feet * 0.3048 + inch * 0.0254
weight = w * 0.453592


bmi = weight / ((height) ** 2)
print("BMI is {}".format(bmi))

if bmi <= 18.5:
    print("You're underweight!")
elif bmi > 18.5 and bmi <= 25.9:
    print("You're normal.")
elif bmi > 25 and bmi <= 29.9:
    print("You're overweight!")
elif bmi > 30 and bmi <= 39.9:
    print("You're obsese!")
    
else:
    print("Monster!")
