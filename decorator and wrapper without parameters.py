# 1. Create a function start_system()
#     Write a decorator that prints:
#     * “System starting…” before execution
#     * “System started successfully” after execution

# def start_system():
#     print("System Started Successfully")
# def decorator(func):
#     print("System starting")
#     def wrapper():
#         print("The system work is on going")
#         func()
#     return wrapper
# func=start_system   if we use functional reference then it will apply only for that particular function so we use the decorator along with parameter and arguments.
# final=decorator(start_system)
# final()
# final()


# def start_system():
#     print("System Started Successfully")
# def decorator(func):
#     print("System starting")
#     def wrapper():
#         print("The system work is on going")
#         func()
#     return wrapper
# final=decorator(start_system)
# final()
# final()


# 2.     Create a function show_message()
#     Write a decorator that prints:
#     * “Welcome!” before
#     * “Goodbye!” after

# def show_message():
#     print("this cvcorp ur career partner")
# def decorator(func):
#     print("welcome!")
    # x = 30
    # print(x)
    # def wrapper():
    #     print("hii good mrng!")
    #     func()
    #     print("Goodbye!")
    # return wrapper
# func=show_message
# x = 20
# my_func=decorator(start_system)
# my_func()

# my_func()


# def show_message():
#     print("this cvcorp ur career partner")
# def decorator(func):
#     print("welcome!")
#     def wrapper():
#         print("hii good mrng!")
#         func()
#         print("Goodbye!")
#     return wrapper
# my_func=decorator(start_system)
# my_func()
# my_func()


# 3.     Create a function make_payment()
#     Write a decorator that prints:
#     * “Payment initiated”
#     * “Payment successful”

# def make_payment():
#     print("payment is ongoing")
# def decorator():
#     print("payment initiated")
#     def wrapper():
#         print("payments started")
#         func()
#         print("payment successful")
#     return wrapper
# func=make_payment
# my_func=decorator()
# my_func()


# def make_payment():
#     print("payment is ongoing")
# def decorator():
#     print("payment initiated")
#     def wrapper():
#         print("payments started")
#         func()
#         print("payment successful")
#     return wrapper
# my_func=decorator(make_payment)
# my_func=decorator(start_system)
# my_func=decorator(show_message)
# my_func()




