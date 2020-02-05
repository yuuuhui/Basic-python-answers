def printChar(ch1,ch2,numberPerLine):
    for x in range(ch1,ch2):
        print(chr(x),end = " ")
        if (x + 1 - ch1) % 10 == 0:
            print("\n")
        else:
            pass



printChar(65,90,10)
