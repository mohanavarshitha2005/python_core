# def greet(name):
#     print("Hi!",name)
# def decorator(func):
#     def wrapper(*args,**kwargs):
#         func(*args,**kwargs)
#         print("function called")
#     return wrapper
# greet=decorator(greet)
# greet("mohana")

# short hand way/short hand format   here @decorator is act as a function is called along with the parameter in the decorator function
# syntax for short hand way is @functionname that which we want to call

# @decorator
# def greet(name):
#     print("Hi!",name)
# def decorator(func):
#     def wrapper(*args,**kwargs):
#         func(*args,**kwargs)
#         print("function called")
#     return wrapper
# greet("mohana")


# def add(a,b):
#      print(a+b)
# def decorator(func):
#     def wrapper(*args,**kwargs):
#         func(*args,**kwargs)
#         print("function called")
#     return wrapper
# greet=decorator(add)
# greet(10,20)


# short hand way/short hand format   here @decorator is act as a function is called along with the parameter in the decorator function
# syntax for short hand way is @functionname that which we want to call

# @decorator
# def add(a,b):
# #      print(a+b)
# def decorator(func):
#     def wrapper(*args,**kwargs):
#         func(*args,**kwargs)
#         print("function called")
#     return wrapper
# add("mohana")