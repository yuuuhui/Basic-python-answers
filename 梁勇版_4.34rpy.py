
x = str(input("Enter a hex character:"))
if x == "1" or \
   x == "2" or \
   x == "3" or \
   x == "4" or \
   x == "5" or \
   x == "6" or \
   x == "7" or \
   x == "8" or \
   x == "9" or \
   x == "a" or \
   x == "b" or \
   x == "c" or \
   x == "d" or \
   x == "e" or \
   x == "f" or \
   x == "A" or \
   x == "B" or \
   x == "C" or \
   x == "D" or \
   x == "E" or \
   x == "F":
    print("The decimal value is {}".format(int(x,16)))
else:
    print("Wrong input!")
