def f_to_c(t):
    return 5*(t-32)/9
t=int(input("Enter temp in F:"))
c=f_to_c(t)
print(round(c,2),"°C")
     