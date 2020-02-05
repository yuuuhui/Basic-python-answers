x2,y2 = eval(input("Enter a point's x- and y- coordinates: "))

x1,y1 = 0,0
x3,y3 = 0,100
x4,y4 = 200,0


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
'''
如果有交点：
    如果不是延长交点：
    在外面
    如果是延长交点：
    在里面
'''


h = a * d - b * c

if h == 0:
    print("The point is not in the triangle")
else:
    x = (e * d - b * f) /(a * d - b * c)
    y =  (a * f - e * c) / (a * d - b * c)
    #print("The intersecting point is at ({:.5f},{:.5f})".format(x,y))
    lengthin = (x ** 2 + y ** 2) ** 0.5
    lengthx2y2 = (x2 ** 2 + y2 ** 2) ** 0.5
    if lengthin >= lengthx2y2:
        print("The point is in the triangle")
    else:
        print("The point is not in the triangle")






        
