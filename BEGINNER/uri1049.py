n01 = input()
n02 = input()
n03 = input()

if(n01 == 'vertebrado'):
    if(n02 == 'ave'):
        if(n03 == 'carnivoro'):
            print('aguia')
        else:
            print('pomba')
    else:
        if(n03 == 'onivoro'):
            print('homem')
        else:
            print('vaca')
else:
    if(n02 == 'inseto'):
        if(n03 == 'hematofago'):
            print('pulga')
        else:
            print('lagarta')
    else:
        if(n03 == 'hematofago'):
            print('sanguessuga')
        else:
            print('minhoca')