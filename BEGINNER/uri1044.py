A = input().split()

a0=int(A[0])
a1=int(A[1])

if (a1 % a0 == 0) or (a0 % a1 == 0) :
    print("Sao Multiplos")
else:
    print("Nao sao Multiplos")