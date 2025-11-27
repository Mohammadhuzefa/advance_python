# class Student:
#     '''Student object data'''
#     school_name='SHSS'
#     def __init__(self):
#         print("Constructer called")
# print(id(Student))
# print(Student.school_name)

# class Student:
#     pass
# print(id(Student))
# obj1=Student
# print(id(obj1))
# obj2=Student
# print(id(obj2))

# class Student:
#     pass
# print(dir(Student))

# class Student:
#     '''This is oop's concept'''
#     x=10
#     y=20
#     z=30
#     def show():
#         print("this is oop's class")
#     print(dir(Student))
    # print(Student.__doc__)
    # print(Student.__module__)
    # print(Student.__dict__)
    # print(Student.__init__) 

# class Student:
#     pass
# print(id(Student))
# obj1=Student
# print(id(obj1))
# obj2=Student()
# print(id(obj2))

# class Student:
#     school='SHSS'
#     def __init__(self):
#         print("constructer called")
#         print(id(self))
# print(id(Student))
# obj=Student()
# print(id(obj))
# obj1=Student()
# print(id(obj1))

class Student:
    scholl ='SHSS' #declaration
    def __init__(self,name,roolno):
        self.n=name
        self.r=roolno
        print(Student.scholl) #Calling
        Student.principal='python'  #declaration
    def addnew(self):
        Student.scholl_code=101 #declaration
    def show(self):
        print(Student.scholl, Student.principal,Student.scholl_code)  #Calling
    @classmethod
    def create_or_update(cls): #declaration
        print(Student.scholl,Student.principal,Student.scholl_city) #Calling
obj=Student("neeraj",111)
obj.addnew()
obj.show()
# obj.create_or_update()
Student.scholl_city='Bhopal'   #declaration
obj.create_or_update()
print(Student.scholl) #Calling
        


    

