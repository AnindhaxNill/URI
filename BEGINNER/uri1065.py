list = []
list.append(int(input()))
list.append(int(input()))
list.append(int(input()))
list.append(int(input()))
list.append(int(input()))

count= 0

for v in list:
    if(v%2 == 0):
        count += 1

print("%d valores pares" %count)