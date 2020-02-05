a = "星期一"
b = "星期二"
c = "星期三"
d = "星期四"
e = "星期五"
f = "星期六"
g = "星期天"

year = int(input("Enter year:(e.g. 2008)"))
month = int(input("Enter month 1 -12"))
m = month + 12
q = int(input("Enter the day of the month: (1 -31)"))
j = year // 100
k = year % 100



h  = (      q + (    26 * (m + 1) // 10    ) +
         k + (  k // 4  ) + (  j // 4  ) + (  5 * j  )     ) % 7


if year > 0:
    if 1 <= month <= 12:
        if 1 <= q <= 31:
            if h == 0:
                print("Day of the week is {}".format(f))
            if h == 1:
                print("Day of the week is {}".format(g))
            if h == 2:
                print("Day of the week is {}".format(a))
            if h == 3:
                print("Day of the week is {}".format(b))
            if h == 4:
                print("Day of the week is {}".format(c))
            if h == 5:
                print("Day of the week is {}".format(d))
            if h == 6:
                print("Day of the week is {}".format(e))
            else:
                print("programming error!")
                
                
        else:
            print("Wrong day input!")
    else:
        print("Wrong month input")
else:
    print("Wrong year input!")
