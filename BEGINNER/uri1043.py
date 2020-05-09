# A = list(map(float,input().split()))
#
# a0=A[0]
# a1=A[1]
# a2=A[2]
#
# if a0+a1>a2 and a0+a2>a1 and a1+a2>a0:
#     x=a0+a1+a2
#     print("Perimetro = ","{:.1f}".format(x))
# else:
#     x= ((a0+a1)/2)*a2
#     print("Area = ","{:.1f}".format(x))

val = input().split()
val = list(map(float,val))

A, B, C = val

if(A+B > C and B+C > A and A+C > B ):
    print("Perimetro = %.1f" %(A+B+C))
else:
    print("Area = %.1f" %(0.5*(A+B)*C))