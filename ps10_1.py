class Programmer:
    company="Microsoft"
    def __init__(self,name,salary,pin) :
        self.name=name
        self.salary=salary
        self.pin=pin

p=Programmer("Harry",1200000,234556)
print(p.name,p.salary,p.pin,p.company)
q=Programmer("Rohan",1200000,234556)
print(q.name,q.salary,q.pin,q.company)
