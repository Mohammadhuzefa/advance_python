# x=range(1000)
# print(list(x))

# def gen_number(n):
#     i=1
#     for i in range(1,n+1):
#         yield i
# n=100
# var=gen_number(n)
# print(var)
# ele1=next(var)
# print(ele1)
# print("hello")
# print("Welcome")
# ele2=next(var)
# print(ele2)

# for i in var:
#     print(i)

# l=list(range(1,10))
# x=iter(l)
# print(x)
# print(next(x))
# print("hello")
# print(next(x))

# l=list(range(1,10))
# x=iter(l)
# for i in x:
#     print(i)
# print(next(x))

l=list(range(1,10))
x=iter(l)
for i in range(15):
    try:
        print(next(x))
    except StopIteration:
        print("itrater is empty")
        break



# x=1
# y=0
# try:
#     z=x/y
#     print(z)
# except ZeroDivisionError:
#     print("Please enter non-zero value aganist y")