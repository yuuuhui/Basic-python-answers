isdate = " "

def year():
    
    year = int(input("Enter year:"))
    while year < 0:
        year = int(input("Enter year:"))
    else:
        pass
    return year

def month():
    month = int(input("Enter month(1 - 12):"))
    while month < 1 or month > 12:
        month = int(input("Enter month(1 - 12):"))
    else:
        pass
    return month
def day():
    day = int(input("Enter the day of the month:"))
    while day < 0:
        day = int(input("Enter the day of the month:"))
    else:
        pass
    return day
def namedate(n):
    
    
    if n == 0:
        
        isdate = "Saturday"
        
    elif n == 1:
        
        isdate = "Sunday"
    elif n == 2:
        
        isdate = "Monday"
    elif n == 3:
    
        isdate = "Tuesday"
    elif n == 4:
        
        isdate = "Wednesday"
    elif n == 5:
       
        isdate = "Thursday"
    elif n == 6:
        
        isdate = "Friday"
    else:
       
        isdate = "error"
    print(isdate)
def date():
    y = year()
    j = y // 100
    k = y % 100
    m = month()
    q = day()
    h = (q + (26 * (m + 1) // 10) + k + (k // 4) + (j // 4) + 5 * j ) % 7
    namedate(h)



    
        
    
date()


