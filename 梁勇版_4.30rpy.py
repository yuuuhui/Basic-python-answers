import time

currenttime = time.time()


totalsecond = int(currenttime)

currentsecond = totalsecond % 60

totalminutes = totalsecond // 60

currentminute = totalminutes % 60

totalhours =  totalminutes // 60

currenthour = totalhours % 24



print("current time is {}:{}:{} GMT" .format(currenthour,currentminute,currentsecond))


time =int(input("Enter the time zone offset to GMT:"))
currenthoura = currenthour + time
if currenthoura > 12:
    currenthoura -= 12
    print("The current time is {}:{}:{}PM".format(currenthoura,currentminute,currentsecond))
else:
    print("The current time is {}:{}:{}AM".format(currenthoura,currentminute,currentsecond))
    
