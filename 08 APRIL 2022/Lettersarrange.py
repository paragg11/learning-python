def getKey(x):
    if x.islower():
        return (2,x)

    elif x.isupper():
        return (4,x)

    elif x.isdigit() :
        if int(x)%2==1:
            return (3,x)
        else:
            return (1,x)

print(*sorted(input(),key=getKey),sep='')