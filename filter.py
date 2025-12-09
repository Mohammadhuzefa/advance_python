# filter syntex:
# Iterable
# def fun_name(n):
#     _______
#     _______
#     _______
#     return
# res=filter(fun_name,Iterable)
# print(list(res))

# s=[50,60,70,65,40,30,90]
# def first_division(n):
#     if n>=60:
#         return n
# print(list(filter(first_division,s)))


# x=eval(input("enter a number"))
# def even_num(n):
#     if n%2==0:
#         return n
# print(list(filter(even_num,x)))


# s=input("enter any number:")
# def vovel(n):
#     if n in ('a','e','i','o','u','A','E','I','O','U'):
#         return n
# res=list(filter(vovel,s))
# print(''.join(res))

# s=input("enter a number:")
# s1=''
# for i in s:
#     if i in ('a','e','i','o','u','A','E','I','O','U'):
#         s1=''.join([s1,i])
# print(s1)

s=input("enter a number:")
v=c=0
for i in s:
    if i in ('a','e','i','o','u','A','E','I','O','U'):
        v=v+1
    elif i=='':
        pass
    else:
        c=c+1
