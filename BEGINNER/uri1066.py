list = []
count = 0
for i in range(5):
    ele = int(input())
    list.append(ele)

even = 0
odd = 0
positive = 0
negative = 0

for v in list:
    if (v % 2 == 0):
        even += 1
    else:
        odd += 1

    if (v > 0):
        positive += 1
    else:
        if (v < 0):
            negative += 1

print("%d valor(es) par(es)" % even)
print("%d valor(es) impar(es)" % odd)
print("%d valor(es) positivo(s)" % positive)
print("%d valor(es) negativo(s)" % negative)