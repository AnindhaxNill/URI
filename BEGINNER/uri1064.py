list = []
list.append(float(input()))
list.append(float(input()))
list.append(float(input()))
list.append(float(input()))
list.append(float(input()))
list.append(float(input()))

positive = 0
count = 0.0

for v in list:
    if(v>0):
        positive += 1
        count += v

media = count / float(positive)
print("%d valores positivos" %positive)
print("%.1f" %media)