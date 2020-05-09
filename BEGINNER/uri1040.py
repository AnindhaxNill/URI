a,b,c,d = [float(item) for item in input().split(" ")] # input a,b,c,d

avg = float(((a*2.00) + (b*3.00) + (c*4.00) + d*1.00) / 10.0) # As given in description
print("Media:",format(avg, '.1f'))

# logical implementations

if( avg >= 7.0 ):
	print("Aluno aprovado.")
elif( avg >= 5.0 and avg <= 6.9 ):
	print("Aluno em exame.")
	e = float ( input() )
	avg2 = float( (avg + e)/2.0 )
	print("Nota do exame: {}".format(e,'.1f'))

	if avg2 >= 5.0:
		print("Aluno aprovado.")
	else:
		print("Aluno reprovado.")

	print("Media final: {}".format(avg2,'.1f'))

else:
	print("Aluno reprovado.")