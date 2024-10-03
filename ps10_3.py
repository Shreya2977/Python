class Demo:
    a = 4
o=Demo()
print(o.a) #prints the class attribute
o.a=0
print(o.a) #prints the instance attribute
print(Demo.a)