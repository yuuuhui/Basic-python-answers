import time

x = time.time()


totalsecond = int(x)

currentsecond = totalsecond % 60

totalminutes = totalsecond // 60

currentminutes = totalminutes % 60

totalhours = totalminutes // 60

currenthours = totalhours % 24

totaldays = totalhours // 24



count = 0
countleap = 0
for year in range(0,100):
    if totaldays < 365:
        break
    elif (year + 1970) % 4 == 0 and (year + 1970) % 100 != 0 \
       or (year + 1970) % 400 == 0:
        totaldays -= 366
        countleap += 1
        
    else:
        
        totaldays -= 365
        count += 1


year = countleap + count +  1970

currenttotaldays = totaldays + 1



if (year + 1970) % 4 == 0 and (year + 1970) % 100 != 0 \
       or (year + 1970) % 400 == 0:
    if currenttotaldays < 31:
        currentmonth = 1
    elif currenttotaldays <60:
        currentmonth = 2
        currenttotaldays -= 31
    elif currenttotaldays <91:
        currentmonth = 3
        currenttotaldays -= 60
    elif currenttotaldays <121:
        currentmonth = 4
        currenttotaldays -= 91
    elif currenttotaldays <152:
        currentmonth = 5
        currenttotaldays -= 121
    elif currenttotaldays <182:
        currentmonth = 6
        currenttotaldays -= 152
    elif currenttotaldays <213:
        currentmonth = 7
        currenttotaldays -= 182
    elif currenttotaldays <244:
        currentmonth = 8
        currenttotaldays -= 213
    elif currenttotaldays <274:
        currentmonth = 9
        currenttotaldays -= 244
    elif currenttotaldays <305:
        currentmonth = 10
        currenttotaldays -= 274
    elif currenttotaldays <335:
        currentmonth = 11
        currenttotaldays -= 305
    elif currenttotaldays <366:
        currentmonth = 12
        currenttotaldays -= 335
    
    
        
        
else:
    if currenttotaldays < 31:
        currentmonth = 1
        
    elif currenttotaldays <59:
        currentmonth = 2
        currenttotaldays -= 31
    elif currenttotaldays <90:
        currentmonth = 3
        currenttotaldays -= 59
    elif currenttotaldays <120:
        currentmonth = 4
        currenttotaldays -= 90
    elif currenttotaldays <151:
        currentmonth = 5
        currenttotaldays -= 120
    elif currenttotaldays <181:
        currentmonth = 6
        currenttotaldays -= 151
    elif currenttotaldays <212:
        currentmonth = 7
        currenttotaldays -= 181
    elif currenttotaldays <243:
        currentmonth = 8
        currenttotaldays -= 212
    elif currenttotaldays <273:
        currentmonth = 9
        currenttotaldays -= 243
    elif currenttotaldays <304:
        currentmonth = 10
        currenttotaldays -= 273
    elif currenttotaldays <334:
        currentmonth = 11
        currenttotaldays -= 304
    elif currenttotaldays <365:
        currenttotaldays -= 334
        currentmonth = 12
    
        
       

currenthours += 8

print("the time is {}/{}/{} ,{}:{}:{}".format(currenttotaldays,currentmonth,year,currenthours,currentminutes,currentsecond))
