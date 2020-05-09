# x=input().split()
# # a,b,c = list(map(float,input().split()))
# a=float(x[0])
# b=float(x[1])
# c=float(x[2])
# print(a)
# print(b)
#
# d = b * b - 4 * a * a
# e = pow(d, .5)
# if (d < 0 or a == 0):
#     print("Impossivel calcular")
# else:
#     f = (-b + e) / (2 * a)
#     g = (-b - e) / (2 * a)
#     print("R1 = " + str("{:.5f}".format(f)))
#     print("R2 = " + str("{:.5f}".format(g)))




# x=input().split()
# a=float(x[0])
# b=float(x[1])
# c=float(x[2])
# if a != 0 and (b**2 - 4*a*c) >= 0:
#     x1 = (-b + ((b**2 - 4*a*c) ** (1/2)))/ 2*a
#     print("R1 = " + str("{:.5f}".format(x1)))
#     x2 = (((-b) - (((b**(2)) - (4*a*c))** (1/2))) / 2*a)
#     print("R2 = "  "{:.5f}".format(x2))
# else:
#     print("Impossivel calcular")


import math
value = input().split()
A, B, C = value

A = float(A)
B = float(B)
C = float(C)

r1 = 0
r2 = 0

cal = (B**2)-(4*A*C)

if(cal <0 or A==0):
    print("Impossivel calcular")
else:
    cal=math.sqrt(cal)
    r1 = (-B+cal)/(2*A)
    r2 = (-B-cal)/(2*A)
    print("R1 = %.5f\nR2 = %.5f" %(r1,r2))





