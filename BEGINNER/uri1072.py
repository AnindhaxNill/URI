r = int(input())
i = 0
o = 0
for e in range(r):
    value = int(input())
    if(value >= 10 and value <= 20):
        i+=1
    else:
        o+=1

print("%d in" %i)
print("%d out" %o)


