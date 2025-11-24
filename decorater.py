# def oute_fun (ver):
#     def inner_fun(x,y):
#         x=x+5
#         y=y+5
#         ver(x,y)
#     return inner_fun
# @oute_fun
# def add(p,q):
#     print(p+q)
# x=2
# y=3
# add(x,y)

# <= Odd number =>
def oute_fun (ver):
    def inner_fun(x):
        ver(x)
        value=range(1,x+1,2)
        return list(value)
    return inner_fun
@oute_fun
def add(n):
    x=range(2,n+1,2)
    return list(x)
n=10
res=add(n)
print(res)