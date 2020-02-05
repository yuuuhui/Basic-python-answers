print("miles \t kg \t  miles  kg")
miles = 1
kg = 20
while (miles in range(1,11)) and (kg in range(20,66)):
    print(str(format(miles,"<2.0f")) +"\t" + str(format(miles * 1.609,">6.3f")) + "\t" +
          str(format(kg /1.609,">6.3f")) + "\t" + str(format(kg,">6.3f")))
    miles += 1
    kg += 5
