try:
    a=int(input("a:"))
    b=int(input("b:"))
    print(a/b)
except ZeroDivisionError as v:
    print("Infinite")