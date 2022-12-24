import os
os.system("cls" if os.name=="nt" else "clear")
# print("hello")


# def yazdir(data):
#     for i in data:
#         print(i ,":",type(i))

# test = ["a",2,3,True,"data",[]]
# yazdir(test)

# class tanımlama

# class Person :
#     name = "victor"
#     age = 22

# person1 = Person()
# person2 = Person()
# print(person1.name)
# person1.name="enes"
# person1.ekleme="ekleme"
# print(person1.name)
# print(person1.ekleme)


# class Person:
#     name= "enes"
#     age = 22

# person1 = Person()


# -----------SELF---------------
# class Person:
#     company="clarusway"
#     name= "enes"
#     def test(self):
#         print("a")

# person1= Person()
# person2 = Person()
# person1.test()


# ------------SPECİAL METAODS---------

    # ---------__init__ ------

# class Person:
#     company="clarusway"

#     def __init__(self,name,age) :
#         self.name=name
#         self.age=age

    
#     def get_details(self):
#         print(f"{self.name}-{self.age}")



# person1 = Person("enes",25 )

# ---------- __str__ ---------

# class Person:
#     comany = "clarusway"
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age

#     def __str__(self) :
#         return f"{self.name}-{self.age}"
    
#     def yazdir(self):
#         print(f"{self.name}-{self.age}")

# person1 =Person("enes",25)
# print(person1) 


# ------------İnheritance--miras---------

# class Person:
#     company = "clarusway"

#     def __init__(self,name,age):
#         self.name=name
#         self.age=age

#     def __str__(self) -> str:
#         return f"{self.name}-{self.age}"

# class Employe(Person):
#     isim="mary"

# emp1=Employe("enes",25)
# print(emp1)

