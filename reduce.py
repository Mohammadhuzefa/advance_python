# import functools
# l=[1,2,3,4,5,6,7]
# def sum (x,y):
#     print(x,y)
#     return x+y
# res=functools.reduce(sum,l,0)
# print(res)

# import functools
# l=[1,2,3,4,5,6,7]
# def sum (x,y):
#     print(x,y)
#     return x+y
# res=functools.reduce(sum,l)
# print(res)

import functools
l=[10,5,20,7,25,8,2]
def max_digit(x,y):
    if x>y:
      return x
    else:
       return y
res=functools.reduce(max_digit,l)
print(res)

