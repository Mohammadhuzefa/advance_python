# class Parent:
#     car='nexon'
#     def home(self):
#         print("home frome parent")
# class Child(Parent):
#     car='Altroz'
#     def home(self):
#         print("home frome chaild")
# obj=Child()
# print(obj.car)
# obj.home


# class Parent:
#     car='Nexon'
#     def home(self):
#         print("Home frome parent")
# class Child(Parent):
#     car='Altroz'
#     car2=Parent.car
#     def home(self):
#         # print(super().car)
#         super().home()
#         print("Home frome chaild")
# obj=Child()
# print(obj.car)
# obj.home()
# print(obj.car2)


#Multi-level ->

# class GrandParent:
#     car = 'Nexon'
#     def home(self):
#         print("Home from GP")
# class Parent:
#     bank='ICICI'
#     def land(self):
#         print("Land fron Parent")
# class Child(GrandParent,Parent):
#     pass
# obj=Child()
# print(obj.car,obj.bank)
# obj.land()
# obj.home()

# class Father:
#     def home(self):
#         print("Home from Father ")
#         Mother.home(self)
# class Mother:
#     def car(self):
#         print("Car from Mother")
#     def home(self):
#         print("home from Mother")
#         # Father.home(self)
# class Child(Father,Mother):
# # class Child(Mother,Father):
#     pass
# obj=Child()
# obj.car()
# obj.home()

# class Parent:
#     def home(self):
#         print("home from parent")
#     def car(self):
#         print("car from parent")
# class Child1(Parent):
#     pass
# class Child2(Parent):
#     pass
# obj1=Child1()
# obj2=Child2()
# obj1.car()

class Parent:
    def home(self):
        print("home from parent")
    def car(self):
        print("car from parent")
class child1(Parent):
    def bank(self):
        print("bank")
class child2(Parent):
    def land(self):
        print("land from child2")
class child(child1,child2):
    pass
obj=child()
obj.bank()
obj.car()
obj.home()
obj.land()



