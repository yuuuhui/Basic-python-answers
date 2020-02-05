w = eval(input("Enter weight in pounds:"))
h = eval(input("Enter height in inches:"))
wc = w * 0.45359237
hc = h * 0.0254
bmi = wc / (hc ** 2)
print("BMI is {:.4f}".format(bmi))
