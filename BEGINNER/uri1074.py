r = int(input())

for e in range(r):
    value = int(input())
    if(value%2 == 0):
        if(value == 0):
            print("NULL")
        if(value > 0):
            print("EVEN POSITIVE")
        else:
            if(value < 0):
                print("EVEN NEGATIVE")
    else:
        if(value> 0):
            print("ODD POSITIVE")
        else:
            print("ODD NEGATIVE")