def footToMeter(foot):
    meter = 0.305 * foot
    print("{:.3f}".format(meter),end ="\t")
def meterTofoot(meter): 
    foot = meter/0.305
    print("{:.3f}".format(foot),end ="\t")

print("Feet \t Meter \t Meter \t Foot")
k = 20.0
for i in range(1,11,1):
    print("{:.3f}".format(i),end = "\t")
    footToMeter(i)
    k -= 5
    print("{:.3f}".format(k),end = "\t")
    meterTofoot(k)
    
    
    print("\n")
    

