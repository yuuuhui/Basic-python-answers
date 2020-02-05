day = int(input("Enter today's day :"))
daye = int(input("Enter the number of days elaspsed since today:"))
dayf = day + daye
dayc = dayf % 7
print(dayc)



if day == 0:
    print("Today is Sunday")
elif day == 1:
    print("Today is Monday")
elif day == 2:
    print("Today is Tuesday")
elif day == 3:
    print("Today is Wednesday")
elif day == 4:
    print("Today is Thursday")
elif day == 5:
    print("Today is Friday")
elif day == 6:
    print("Today is Saturday")

else:
    print("Wrong input")


if dayc == 0:
    print("The future day is Sunday")
elif dayc == 1:
    print("The future day is Monday")
elif dayc == 2:
    print("The future day  is Tuesday")
elif dayc == 3:
    print("The future day is Wednesday")
elif dayc == 4:
    print("The future day is Thursday")
elif dayc == 5:
    print("The future day is Friday")
elif dayc == 6:
    print("The future day is Saturday")
else:
    print("no else")


