# l=[80,30,70,60]
# print(list(map(lambda x: f'{int((x*9/5)+32)}F',l)))

# l=['Hii','hello','Bye',"gdmrng"]
# print(list(filter(lambda x:x==x.capitalize(),l)))


# from functools import reduce
# l=[1,2,3,4,5]
# print(reduce(lambda x,y:x*y,l))


# l=[{'name':'mohana','age':19},
#    {'name':'asha','age':22},
#    {'name':"vasavi",'age':20}]
# print(sorted(l,key=lambda x:x['age'],reverse=True))



# def square(x):
#     return x**2
# def cube(x):
#     return x**3
# def my_map(func,lst):
#     for i in lst:
#         if i!=0:
#             print(func(i),end=" ")
# l=[2,3,4,5]
# my_map(square,l)

# l=[2,3,4,5]
# print(list(map(lambda x:x**2,l)))


from functools import reduce
l=['cat','elephant','dog','rhinoceros']
print(reduce(lambda x,y:x if len(x)>len(y) else y,l))
