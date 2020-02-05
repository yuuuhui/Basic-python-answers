print("angle \t Sin \t Cos ")
from math import *
for i in range(0,361,10):
    print(str(format(i,"<3.0f")) + "\t" + str(format(sin(i),">7.4f")) + "\t" + str(format(cos(i),">7.4f")))
