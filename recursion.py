#basic syntax
#def fun_name(parameters)
    #base case / terminating point
    #if condition
        #return
    #recursion point
    #fun_name(modifire parameters)

#fun_name(argument)


# def netural_no(n):
#     if n==0:
#         return
#     netural_no(n-1)
#     print(n)
# n=10
# netural_no(n)

# def even_no(n):
#     if n==0:
#         return None
#     even_no(n-1)
#     print(2*n)
# n=10
# even_no(n)

# def sum_netural_no(n):
#     if n==1:
#         return 1
#     return n+sum_netural_no(n-1)
    
# n=10
# res=sum_netural_no(n)
# print(res)

# def sum_even_no(n):
#     if n==1:
#         return 2*n
#     return 2*n+sum_even_no(n-1)
    
# n=10
# res=sum_even_no(n)
# print(res)

# def sum_odd_no(n):
#     if n==1:
#         return 2*n-1
#     return 2*n+sum_odd_no(n-1)
    
# n=10
# res=sum_odd_no(n)
# print(res)

# def multi(n):
#     if n==1:
#         return 1
#     return n*multi(n-1)
    
# n=5
# res=multi(n)
# print(res)

#factorial number 
def factorial(n):
    if n==1:
        return 1
    return n*factorial(n-1)
    
n=5
res=factorial(n)
print(res)