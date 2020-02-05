#闰年和非闰年 
year = int(input("Enter the year:"))
month = str(input("Enter the month:"))
if year < 0:
    print("wrong input!")
elif year % 4 == 0 and month =="二月":
    print("{}年{}月有29天".format(year,month))
else:
    if month == "一月":
        print("{}年{}份有31天".format(year,month))
    elif month == "二月":
        print("{}年{}份有28天".format(year,month))
    elif month == "三月":
        print("{}年{}份有31天".format(year,month))
    elif month == "四月":
        print("{}年{}份有30天".format(year,month))
    elif month == "五月":
        print("{}年{}份有31天".format(year,month))
    elif month == "六月":
        print("{}年{}份有30天".format(year,month))
    elif month == "七月":
        print("{}年{}份有31天".format(year,month))
    elif month == "八月":
        print("{}年{}份有31天".format(year,month))
    elif month == "九月":
        print("{}年{}份有30天".format(year,month))
    elif month == "十月":
        print("{}年{}份有31天".format(year,month))
    elif month == "十一月":
        print("{}年{}份有30天".format(year,month))
    elif month == "十二月":
        print("{}年{}份有31天".format(year,month))
    else:
        print("输入错误")
