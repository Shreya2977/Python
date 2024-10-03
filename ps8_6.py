def rem(l,word):
    n=[]
    for item in l:
        if not(item==word):
            n.append(item)
    return n

l = ["Harry","Rohan","Shumbham","an"]
print(rem(l,"an"))