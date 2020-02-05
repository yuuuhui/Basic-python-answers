

millis = eval(input("Enter millis:"))
def convertmillis(millis):
    totalsecond = millis  // 1000
    currentsecond = totalsecond % 60

    currentminutes = totalsecond // 60

    totalminutes = currentsecond % 60
    currenthours = totalminutes // 60

    print("{}:{}:{}".format(currenthours,currentminutes,currentsecond))


convertmillis(millis)
