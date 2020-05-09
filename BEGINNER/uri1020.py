days = int(input())

years = int(days / 365)
days -= years * 365
print(days)
months = int(days / 30)
days -= months * 30

print(repr(years) + " ano(s)")
print(repr(months) + " mes(es)")
print(repr(days) + " dia(s)")
#new
valor = int(input())
ano = int(valor / 365)
mes = int((valor % 365 / 30))
dia = int(valor % 365 % 30)

print('%d ano(s)\n%d mes(es)\n%d dia(s)' % (ano, mes, dia))
