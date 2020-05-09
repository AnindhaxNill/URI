notes = int(input())
print(notes)
print("{} nota(s) de R$ 100,00".format(int(notes/100)))
aux = (notes%100)
print("{} nota(s) de R$ 50,00".format(int(aux/50)))
aux = (aux%50)
print("{} nota(s) de R$ 20,00".format(int(aux/20)))
aux = (aux%20)
print("{} nota(s) de R$ 10,00".format(int(aux/10)))
aux = (aux%10)
print("{} nota(s) de R$ 5,00".format(int(aux/5)))
aux = (aux%5)
print("{} nota(s) de R$ 2,00".format(int(aux/2)))
aux = (aux%2)
print("{} nota(s) de R$ 1,00".format(int(aux/1)))

#new
valor = int(input())
hu  = int(valor / 100)
fif = int(valor % 100 / 50)
tw  = int(valor % 100 % 50/20)
te  = int(valor % 100 % 50%20/10)
fiv = int(valor % 100 % 50%20%10/5)
twoe = int(valor % 100 % 50%20%10%5/2)
o =   int(valor % 100 % 50%20%10%5%2)

print(hu,fif,tw,te,fiv,twoe,o)

#new
money= int(input())
hundred = int(money/100)
print(hundred)
money= abs(money-hundred*100)

fifty = int(money/50)
print(fifty)
money= abs(money-fifty*50)

twenty = int(money/20)
print(twenty)
money = abs(money-twenty*20)

ten = int(money/10)
print(ten)
money= abs(money- ten*10)

five = int(money/5)
print(five)
money = abs(money - five*5)

two= int(money/2)
print(two)
money = abs(money - two*2)

one = int (money / 1)
print(one)
