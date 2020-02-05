year = int(input("Enter the year:"))
day = int(input("Enter the date of 1st of the year:"))
m1 = "Monday"
t2 = "Tuesday"
w3 = "Wednesday"
t4 = "Thursday"
f5 = "Friday"
s6  ="Saturday"
s7 = "Sunday"


if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    count = 1
    while count <= 12:
        
        if count == 1:
            newday = day
            print("January 1,{} is ".format(year),end = "")
        elif count == 2:
            newday =  (day + 31) % 7
            print("Febuary 1,{} is ".format(year),end = "")
        elif count == 3:
            newday =  (day + 31 + 29) % 7
            print("March 1,{} is ".format(year),end = "")
        elif count == 4:
            newday = (day + 31 + 29 + 31) % 7
            print("April 1,{} is ".format(year),end = "")
        elif count == 5:
            newday =  (day + 31 + 29 + 31 + 30) % 7
            print("May 1,{} is ".format(year),end = "")
        elif count == 6:
            newday =  (day + 31 + 29 + 31 + 30 + 31) % 7
            print("June 1,{} is ".format(year),end = "")
        elif count == 7:
            newday = (day + 31 + 29 + 31 + 30 + 31 + 30 ) % 7
            print("July 1,{} is ".format(year),end = "")
        elif count == 8:
            newday =  (day + 31 + 29 + 31 + 30 + 31 + 30 + 31) % 7
            print("August 1,{} is ".format(year),end = "")
        elif count == 9:
            newday =  (day + 31 + 29 + 31 + 30 + 31 + 30 + 31 + 31) % 7
            print("September 1,{} is ".format(year),end = "")
        elif count == 10:
            newday = (day + 31 + 29 + 31 + 30 + 31 + 30 + 31 + 31 + 30) % 7
            print("October 1,{} is ".format(year),end = "")
        elif count == 11:
            newday =  (day + 31 + 29 + 31 + 30 + 31 + 30 + 31 + 31 + 30 + 31) % 7
            print("November 1,{} is ".format(year),end = "")
        elif count == 12:
            newday =  (day + 31 + 29 + 31 + 30 + 31 + 30 + 31 + 31 + 30 + 31 + 30) % 7
            print("December 1,{} is ".format(year),end = " ")
        else:
            print("No else")


        if newday == 1:
            nday = m1
        elif newday == 2:
            nday = t2
        elif newday == 3:
            nday = w3
        elif newday == 4:
            nday = t4
        elif newday == 5:
            nday = f5
        elif newday == 6:
            nday = s6
        elif newday == 0:
            nday = s7
        else:
            print("wrong input!")
        print(nday)
            
        count += 1
    



else:
    count = 1
    while count <= 12:
        
        if count == 1:
            newday = day
            print("January 1,{} is ".format(year),end = "")
        elif count == 2:
            newday =  (day + 31) % 7
            print("Febuary 1,{} is ".format(year),end = "")
        elif count == 3:
            newday =  (day + 31 + 28) % 7
            print("March 1,{} is ".format(year),end = "")
        elif count == 4:
            newday = (day + 31 + 28 + 31) % 7
            print("April 1,{} is ".format(year),end = "")
        elif count == 5:
            newday =  (day + 31 + 28 + 31 + 30) % 7
            print("May 1,{} is ".format(year),end = "")
        elif count == 6:
            newday =  (day + 31 + 28 + 31 + 30 + 31) % 7
            print("June 1,{} is ".format(year),end = "")
        elif count == 7:
            newday = (day + 31 + 28 + 31 + 30 + 31 + 30 ) % 7
            print("July 1,{} is ".format(year),end = "")
        elif count == 8:
            newday =  (day + 31 + 28 + 31 + 30 + 31 + 30 + 31) % 7
            print("August 1,{} is ".format(year),end = "")
        elif count == 9:
            newday =  (day + 31 + 28 + 31 + 30 + 31 + 30 + 31 + 31) % 7
            print("September 1,{} is ".format(year),end = "")
        elif count == 10:
            newday = (day + 31 + 28 + 31 + 30 + 31 + 30 + 31 + 31 + 30) % 7
            print("October 1,{} is ".format(year),end = "")
        elif count == 11:
            newday =  (day + 31 + 28 + 31 + 30 + 31 + 30 + 31 + 31 + 30 + 31) % 7
            print("November 1,{} is ".format(year),end = "")
        elif count == 12:
            newday =  (day + 31 + 28 + 31 + 30 + 31 + 30 + 31 + 31 + 30 + 31 + 30) % 7
            print("December 1,{} is ".format(year),end = " ")
        else:
            print("No else")


        if newday == 1:
            nday = m1
        elif newday == 2:
            nday = t2
        elif newday == 3:
            nday = w3
        elif newday == 4:
            nday = t4
        elif newday == 5:
            nday = f5
        elif newday == 6:
            nday = s6
        elif newday == 0:
            nday = s7
        else:
            print("wrong input!")
        print(nday)
            
        count += 1

