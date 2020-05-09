val = input().split()
val = list(map(int,val))
a, b, c, d = val
start= a*60 + b
finish = c*60 +d
du=0


if a==c:
    if b == d:
        print("O JOGO DUROU 24 HORA(S) E 0 MINUTO(S)")
    else:
        if b > d:
            du =finish - start
            print("O JOGO DUROU 23 HORA(S) E %d MINUTO(S)"%(du%60))
        else:
            print("O JOGO DUROU 0 HORA(S) E %d MINUTO(S)" %(d-b))
else:
    if a<c:
        du = finish - start
        print("O JOGO DUROU %d HORA(S) E %d MINUTO(S)" %(du/60,du%60))
    else:
        du = (24*60 - start) + finish
        print("O JOGO DUROU %d HORA(S) E %d MINUTO(S)" % (du / 60, du % 60))