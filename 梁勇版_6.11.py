
def computeCommission():
    print("Sale Amount  | \t Commission")
    for saleamount in range(10000,100000,5000):
        print(saleamount,end = "\t     | \t ")
        if saleamount < 5000:
            rate = 0.08
        elif saleamount < 10000:
            rate = 0.10
        elif saleamount >= 10000:
            rate = 0.20
        print(saleamount * rate)
        




computeCommission()
