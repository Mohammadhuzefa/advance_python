# -> Example of list <-

# n= int(input("enter a number "))
# for i in range (n):
#     print(i)

# # even number 
# n= int(input("enter a number "))
# print([2*i for i in range(1,n+1)])

# # odd number
# n= int(input("enter a number "))
# print([2*i for i in range(1,n-1)])


# n=10
# print([i for i in range(1,n+1) if i%2==0])
# print(["even" for i in range(1,n+1) if i%2==0])

# n=10
# print([('even' if i%2==0 else 'odd') for i in range(1,n+1)])
# print(['even' if n%2==0 else 'odd'])
# print([(('even',i) if i%2==0 else 'odd') for i in range(1,n+1)])

# -> Example of dict <-

n=10
# # print({ i:i**2 for i in range (1,n) if 1%2==0})
print({ i:i**2 for i in range (1,n) if 1%2==0})