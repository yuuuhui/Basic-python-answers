

year =int(input("Enter the year:"))
def numberofDaysInAYear():
    print("year \t  number of days")
    for i in range(2010,2021):
        print(i,end ="\t\t")
        k = 365
        if i % 4 == 0 and i % 100 != 0:
            k = 366
        elif i % 400 == 0:
            k = 366

        else:
            k = 365
        print(k,end = "\n")
        
        
numberofDaysInAYear()
