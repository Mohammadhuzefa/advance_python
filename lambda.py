# x=lambda p,q,r:p+q+r
# x(10,20,30)
# print(x(10,20,30))

# z=x(10,20,30)
# print(z)

# x=lambda p,q,r:print(p+q+r)
# x(10,20,30)

# x=lambda p,q : if-result if condition else else-result
# x=lambda p,q:
# print(x(10,20))

# map with lambda
# multiplication
# l=[1,2,3,4,5]
# print(list(map(lambda n: n*n,l)))

# even & odd
# l=[1,2,3,4,5]
# print(list(map(lambda n:'even' if n%2==0 else 'odd',l)))

# print(list(filter(lambda n:n if n%2==0 else None ,l)))

from functools import reduce
# l=[1,2,3,4,5]
# print(reduce(lambda x,y:x+y,l))

# l=[1,2,3,4,5]
# print(reduce(lambda x,y:x if x>y else y,l))
# l.remove(5)
# print(reduce(lambda x,y:x if x>y else y,l))

# any largest number can want.
l=[1,2,3,4,5]
n=int(input("enter which largest no. you want:"))
if n<=len(l):
    for _ in range(n):
        x=reduce(lambda x,y:x if x>y else y,l)
        l.remove(x)
    print(f'{n} maximum digit is {x}')
else:
    print("plase enter valid option")