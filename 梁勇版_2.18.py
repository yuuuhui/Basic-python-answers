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
print("The current time is {}:{}:{}".format(currenthour + time,currentminute,currentsecond))
