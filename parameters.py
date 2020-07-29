import math
def slope(x1,y1,x2,y2):
    return((y2-y1)/(x2-x1))
while(1):
    x1=int(input())
    y1=int(input())
    x2=int(input())
    y2=int(input())
    x3=int(input())
    y3=int(input())
    m1=slope(x1,y1,x2,y2)
    m2=slope(x2,y2,x3,y3)
    angle=math.degrees(math.atan((m1-m2)/(1+(m1*m2))))
    print(angle)