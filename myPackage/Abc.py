'''
Created on Jan. 18, 2023

@author: sarat
'''






class Abc:

    s = "This is a class"
    print(s)

p = Abc()

p.s="This is an object"
print(p.s)

t = Abc()

t.s="This is second object"
print(t.s)



class Person:
    def __init__(self,Myname):
        self.Myname=Myname
    
        
obj = Person("Sarath")
print(obj.Myname)
        
        

























