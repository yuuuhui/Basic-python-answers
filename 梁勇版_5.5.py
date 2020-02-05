print("  kg \t pounds \t   kg \t  pounds")
k = 9.09
while k < 235:
    for i in range(1,200):
        print(str(format(i,">5.1f")) + str(format(i * 2.2,">10.2f"))  +"\t" + "\t" +
          str(format(k,">6.2f")) + str(format(k * 2.2,">10.2f")))
        k += 2
