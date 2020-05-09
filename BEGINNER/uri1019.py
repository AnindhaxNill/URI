i= int(input())
x="{}".format(int(i/3600))
y = i%3600
z="{}".format(int(y/60))
p = y%60
q="{}".format(int(p))
print(x+":"+z+":"+q)



s = int(input())
h = int(s / 3600)
s-= h * 3600
print(s)
m = int(s / 60)
s -= m * 60

print(repr(h) + " ano(s)")
print(repr(m) + " mes(es)")
print(repr(s) + " dia(s)")
