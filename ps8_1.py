def greatest(a,b,c):
    if(a>b and a>c):
        return a
    elif (b>c and b>a):
        return b
    elif(c>a and c>b):
        return c
a=23
b=67
c=87

print(greatest(a,b,c))
