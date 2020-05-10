def j(n, k):
    if (n == 1):
        return 1
    else:
        return ((j(n-1,k)+k-1)%n)+1

x = int(input())
count = 0
for _ in range(x):
    y = input().split()
    y0 = int(y[0])
    y1 = int(y[1])
    u = j(y0,y1)
    count = count+1
    print("Case ",count,":",u)
