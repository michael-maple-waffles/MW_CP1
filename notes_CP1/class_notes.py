#MW_CP1 classes



class Person:
    #The __init__() method
    def __init__(self,name,age):
        self.name = name
        self.age = age
    #The __str__() method
    def __str__(self):
        return f"{self.name}({self.age})"
    #You can build your own functions
    def myfunc(self):
        print(f"Hello my name is {self.name} and I am {self.age} years old")

#Key things: self isnt required, it can be whatever you want it to be, it just refers to the name of the class itself. so banaGirl could work.

p1 = Person("Josh",72)

print(p1.name+" " +str(p1.age))

print(p1)

p1.myfunc()

#you can also delete certain properties or change them!

del p1.age
p1.age = int(input("How old is josh now?"))

p1.myfunc()

#you can also just straight up delete the variable!

del p1
p1.myfunc()
