# class Student:
#     def __init__(self,name,rollno):
#         self.n=name
#         self.r=rollno
#         x=10
#         print(x)
#     def show(self):
#         y=10
#         print(y)
#         print(x)
# obj=Student('neeraj',101)
# # obj.show()

# class Book:
#     price=100
#     def __init__(self,title,branch):
#         self.t=title
#         self.b==branch
# obj1=Book('python book','IT')
# print(obj1.price)
# obj2=Book('pthon book','IT')
# print(obj2.price)


# class Book:
#     price=100
#     def __init__(self,title,branch):
#         self.t=title
#         self.b==branch
#     @classmethod
#     def update_price(cls,newprice):
#         cls.price=newprice
# obj=Book('python','IT')
# print(obj.price)
# x=float(input("enter new price:"))
# obj.update_price(x)
# print((obj.price))

# class Student:
#     x=10
#     def __init__(self,name):
#         self.n=name
#     @staticmethod
#     def great(name):
#         print(f'welcome {name}')

# obj=Student('neeraj')
# # obj.showdetail()
# x=obj.n
# obj.great(x)

class Parent:
    city='Bhopal'
    def car(self):
        print("Car from parent")
class Child(Parent):
    pass
obj=Child()
print(obj.city)
obj.car()
