money= float(input())

print("NOTAS:")
hundred =int( float(money/100))
print(str(hundred) +" nota(s) de R$ 100.00")
money= abs(money-hundred*100)

fifty = int(float(money/50))
print(str(fifty)+ " nota(s) de R$ 50.00")
money= abs(money-fifty*50)

twenty = int(float(money/20))
print(str(twenty)+ " nota(s) de R$ 20.00")
money = abs(money-twenty*20)

ten = int(float(money/10))
print(str(ten)+ " nota(s) de R$ 10.00")
money= abs(money- ten*10)

five =int(float(money/5))
print(str(five)+" nota(s) de R$ 5.00")
money = abs(money - five*5)

two= int(float(money/2))
print(str(two)+" nota(s) de R$ 2.00")
money = abs(money - two*2)

print("MOEDAS:")

one = int(float(money / 1))
print(str(one)+" moeda(s) de R$ 1.00")
money = abs(money - one*1)


p_fifty = int(float(money/.50))
print(str(p_fifty)+" moeda(s) de R$ 0.50")
money = abs(money - p_fifty*.50)

p_t_five = int(float(money/.25))
print(str(p_t_five)+" moeda(s) de R$ 0.25")

p_ten=int(float(money/.10))
print(str(p_ten)+" moeda(s) de R$ 0.10")
money = abs(money - p_ten*.10)

p_five=int(float(money/.05))
print(str(p_five)+" moeda(s) de R$ 0.05")
money = abs(money - p_five*.05)

p_one=int(float(money/.01))
print(str(p_one)+" moeda(s) de R$ 0.01")
money = abs(money - p_one*.01)