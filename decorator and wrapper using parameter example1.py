# 1.     Create a function get_message() that returns "hello user". Write a decorator using @ syntax that converts the output to uppercase.

# def decorator1(func):
#     def wrapper(*args,**kwargs):
#         print(func(*args,**kwargs).upper())
#         print("converted into uppercase")
#     return wrapper
# @decorator1
# def get_message(name="user"):
#     msg= "hello" +  " " + name
#     return msg
# get_message("mohana")

# 2.     Create a function get_number() that returns 10
#     Use a decorator to return double the value.

# def decorator(func):
#     def wrapper(*args,**kwargs):
#          return 2*func(*args,**kwargs)
#     return wrapper
# @decorator
# def get_number():
#     return 10
# print(get_number())

# 3.     Create a function place_order(item)
#     Use a decorator to print:
#     * “Order process started”
#     * “Order process completed”

# def decorator(func):
#     def wrapper(*args,**kwargs):
#         print("order process started")
#         func(*args,**kwargs)
#     return wrapper
# @decorator
# def place_order(item):
#     print("order process completed :",item)
# place_order("printer")

# def decorator(func):
#     def wrapper(*args,**kwargs):
#         print("Authenticating user")
#         func(*args,**kwargs)
#     return wrapper
# @decorator
# def login(username,password):
#     print("login successful",username,password)
# login(username='mohana',password='123')

# 5.     Create a function send_message(msg)
#     Use a decorator to print:
#     * “Sending message…”
#     * “Message sent”

# def decorator(func):
#     def wrapper(*args,**kwargs):
#         print("sending message")
#         func(*args,**kwargs)
#     return wrapper
# @decorator
# def send_message(msg):
#     print("message sent",msg)
# send_message("hello gd mrng")

# 6.     Create a function add(a, b)
#     Use a decorator to print:
#     * “Calculating sum…”
#     * “Calculation done”

# def decorator(func):
#     def wrapper(*args,**kwargs):
#         print("calculating sum")
#         func(*args,**kwargs)
#     return wrapper
# @decorator
# def add(a,b):
#     print(a+b)
#     print("calculation done")
# add(20,30)

# 7.     Create a function apply_discount(price)
#     Use a decorator to print:
#     * “Applying discount…”
#     * “Discount applied”

# def decorator(func):
#     def wrapper(*args,**kwargs):
#         print("applying discount")
#         func(*args,**kwargs)
#     return wrapper
# @decorator
# def apply_discount(price):
#     if price>5000:
#         print(price-price*0.1)
#         print("discount applied")
#     else:
#         print(price)
#         print("no discount applied")
# apply_discount(15000)
# apply_discount(3000)



