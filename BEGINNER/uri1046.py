val = input().split()
val= list(map(float,val))

h1, h2 = val

if(h1 == h2):
	print('O JOGO DUROU %s HORA(S)' %24)
else:
	if(h2 < h1):
		print('O JOGO DUROU %s HORA(S)' %((24 - h1) + h2))
	else:
		print('O JOGO DUROU %s HORA(S)' %(h2 - h1))