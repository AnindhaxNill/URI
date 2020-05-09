

from math import*
x1=float(input("enter valu of x1: "))
y1=float(input("enter valu of y1: "))
x2=float(input("enter valu of x2: "))
y2=float(input("enter valu of y2: "))
p1=[x1,y1]
p2=[x2,y2]
print(p1,p2)
Distance = ( (p2[0]-p1[0])**(2) + (p2[1]-p1[1])**(2) )**(1/2)
print(round(Distance,4))
print('{:.4f}'.format(Distance)) #for showing 4 digit after decimal


# uri way
p1= input().split()
x1=float(p1[0])
y1 =float(p1[1])

p2= input().split()
x2=float(p2[0])
y2=float(p2[1])

d=( (x2-x1)**(2) + (y2-y1)**(2) )**(1/2)

print('{:.4f}'.format(d))