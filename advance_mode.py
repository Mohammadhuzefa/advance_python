# f=open('x4.txt','x+')
# print(f.name)
# print(f.mode)
# print(f.writable())
# print(f.readable())
# print(f.closed)
# print(f.encoding)

# f=open('w2.txt','w+')
# print(f.name)
# print(f.mode)
# print(f.writable())
# print(f.readable())
# print(f.closed)
# print(f.encoding)

f=open("a1.txt",'a+')
# data = "this is python class"
# f.write(data)
# f.close()

# data1='''This is 
#                 python and
#                           django class\n'''
# f.write(data1)
# f.close()

# data1="This is python class\n"
# data2="This is python class\n"
# data3="This is python class\n"
# f.writelines([data1,data2,data3])
# f.close()

# f=open("a1.txt",'r+')
# data = f.read()
# print(data)
# f.close()
# data1=f.read()
# print("data1:",data1)

# data=f.read(10)
# print(data)
# data1=f.read(5)
# print(data1)
# f.close()

# data=f.readlines()
# print(data)
# f.close()

# data =f.readlines()
# print(data)
# f.close()

# with open('a1.txt','a+')as f:
#     data = 'python'
#     f.write(data)
#     print(f.closed)
# print(f.closed)

# with open('a1.txt','r+')as f:
#     print(f.tell())
#     data=f.read(10)
#     print(data)
#     print(f.tell())

# with open ('x1.txt','ab+')as f:
#     print(f.tell())
#     data= b'this is python class'
#     f.write(data)
#     print(f.tell())
#     data1=f.read()
#     print(data1)
#     f.seek(0,0)
#     print(f.tell())
#     data2=f.read(20)
#     print(data2)
#     print(f.tell())

# with open ('x1.txt','rb+')as f:
#     print(f.tell())
#     f.read(10)
#     print(f.tell())
#     f.seek(-5,1)
#     print(f.tell())

with open('github.docx','rb+')as f:
    print(f.tell())
    data10=f.read(10)
    print(data10)
    print(f.tell())
    f.seek(-5,1)
    print(f.tell())
    f.seek(10,1)
    print(f.tell())
    data5=f.read(5)
    print(data5)
    f.seek(-5,2)
    data5=f.read()
    print(data5)
