x1,y1,x2,y2,x3,y3,x4,y4 = eval(input("Enter x1,y1,x2,y2,x3,y3,x4,y4:"))

a = y1 - y2
b = -(x1 - x2)
c = y3 - y4
d = -(x3 - x4)
e = (y1 - y2) * x1 - (x1 - x2) * y1
f = (y3 - y4) * x3 - (x3 - x4) * y3

'''
print("""
for {}x + {}y = {}
    {}x + {}y = {}
""".format(a,b,e,c,d,f))
'''


h = a * d - b * c

if h == 0:
    print("The two lines are parallel")
else:
    x = (e * d - b * f) /(a * d - b * c)
    y =  (a * f - e * c) / (a * d - b * c)
    print("The intersecting point is at ({:.5f},{:.5f})".format(x,y))
