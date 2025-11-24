# <-Public variable->

# class Parent:
#     bank='HDFC'
#     def add(self):
#         print("hello--")
# class Child(Parent):
#     pass
# obj=Child()
# print(obj.bank)
# obj.add()

# <-Protected variable->

# class Parent:
#     _bank='HDFC'
#     def _add(self):
#         print("hello--")
# class Child(Parent):
#     pass
# obj=Child()
# print(obj._bank)
# obj._add()

# <-Private variable->

class Parent:
    __bank='HDFC'
    def __add(self):
        print("hello--")
class Child(Parent):
    pass
obj=Child()
# print(obj.__bank)
# obj.__add()
# print(Parent.__bank)
print(dir(Parent))
print(obj._Parent__bank)
obj._Parent__add()
