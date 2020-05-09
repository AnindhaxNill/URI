x0= list(map(float,input().split()))

x= x0[0]
y= x0[1]

print(x,y)
if x== 0 and y ==0:
    print("Origem")
elif x== 0 and y !=0:
    print("Eixo Y")
elif x!= 0 and y ==0:
    print("Eixo X")
else:
    if x<0 and y<0:
        print("Q3")
    elif x>0 and y>0:
        print("Q1")
    elif x>0 and y<0:
        print("Q4")
    elif x<0and y>0:
        print("Q2")


