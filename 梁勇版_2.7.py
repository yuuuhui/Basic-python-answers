minute = eval(input("Enter then number of minutes:"))
day = minute / 60 / 24
if day >= 365:
    year = int(day // 365)
    dayc = int(day % 365)
    print("{}minutes is approximately {} years and {} days".format(minute,year,dayc))
else:
    print("{} minutes is approximately {} days".format(minute,int(day)))
    
