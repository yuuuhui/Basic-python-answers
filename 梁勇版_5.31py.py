
year = int(input("Enter the year:"))
day = int(input("Enter the 1st date of the year (0 - 6) for(Sun - Mon)"))
for i in range(1,13):
    if i == 1:
        m = "January"
        nday = 31
        newday = day
    elif i == 2:
        m = "Febuary"
        nday = 28
        newday =  (day + 31) % 7
    elif i == 3:
        m = "March"
        nday = 31
        newday =  (day + 31 + 28) % 7
        
    elif i == 4:
        m = "April"
        nday = 30
        newday = (day + 31 + 28 + 31) % 7
    elif i == 5:
        m = "May"
        nday = 31
        newday =  (day + 31 + 28 + 31 + 30) % 7
    elif i == 6:
        m = "June"
        nday = 30
        newday =  (day + 31 + 28 + 31 + 30 + 31) % 7
    elif i == 7:
        m = "July"
        nday = 31
        newday = (day + 31 + 28 + 31 + 30 + 31 + 30 ) % 7
    elif i == 8:
        m = "August"
        nday = 31
        newday =  (day + 31 + 28 + 31 + 30 + 31 + 30 + 31) % 7
    elif i == 9:
        m = "September"
        nday = 30
        newday =  (day + 31 + 28 + 31 + 30 + 31 + 30 + 31 + 31) % 7
    elif i == 10:
        m = "October"
        nday = 31
        newday = (day + 31 + 28 + 31 + 30 + 31 + 30 + 31 + 31 + 30) % 7
    elif i == 11:
        m = "November"
        nday = 30
        newday =  (day + 31 + 28 + 31 + 30 + 31 + 30 + 31 + 31 + 30 + 31) % 7
    elif i == 12:
        m = "December"
        nday = 31
        newday =  (day + 31 + 28 + 31 + 30 + 31 + 30 + 31 + 31 + 30 + 31 + 30) % 7
        
    else:
        print("error occured!")
    print(newday)
        
    
    print("\t\t {} {}".format(m,year))
    print("\t-------------------------------")
    print("\t  Sun  Mon  Tue  Wed  Thu  Fri  Sat")
    if i == 1:
        print("\t " + "     " * (day),end = " ")
    else:
        print("\t " + "     " * (newday),end = " ")
    
    for k in range(1,nday+1):
            
        print("{:>2}".format(k),end = "   ")
        
    
            
        x = 7 - newday
        if k == x :
            print("\n",end = "\t ")
        elif (k - x ) % 7 == 0:
            print("\n",end = "\t\r ")
            
            
            

 
    print("\n")
    
