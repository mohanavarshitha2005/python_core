# A banking application has a function check_balance(). Create two decorators: verify_user, which prints "User verified", and log_transaction, which prints "Transaction logged". Apply both decorators to check_balance() and display "Balance displayed" from the original function.

# def dec1(func):
#     def wrap1(*args,**kwargs):
#         print("user verified")
#         func(*args, **kwargs)
#     return wrap1
# def dec2(func):
#     def wrap2(*args,**kwargs):
#         func(*args, **kwargs)
#         print("Transaction logged")
#     return wrap2
# @dec1
# @dec2
# def check_balance(amount,balance):
#     if amount>0:
#         print(balance-amount)
#     else:
#         print(balance)
# check_balance(13000,40000)


# An online examination system has a function start_exam(student). Before allowing the student to start the exam, the system must verify the student’s login and then log the exam activity. Create two decorators, login_required and log_activity, and apply both decorators to start_exam(). The function should finally display "Exam started for <student>".

# def dec1(func):
#     def wrap1(*args,**kwargs):
#         print("login required")
#         func(*args,**kwargs)
#     return wrap1
# def dec2(func):
#     def wrap2(*args,**kwargs):
#         print("loging activity")
#         print("student logined")
#         func(*args,**kwargs)
#     return wrap2
# def start_exam(name):
#     print(name,"from py-21 batch")
# start_exam=dec2(start_exam)
# start_exam=dec1(start_exam)
# start_exam("mohana")

# def dec1(func):
#     def wrap1(*args,**kwargs):
#         print("login required")
#         func(*args,**kwargs)
#     return wrap1
# def dec2(func):
#     def wrap2(*args,**kwargs):
#         print("loging activity")
#         print("student logined")
#         func(*args,**kwargs)
#     return wrap2
# # @dec1
# # @dec2
# def start_exam(name):
#     print(name,"from py-21 batch")
#start_exam("mohana")

# An online shopping application has a function place_order(). Create two decorators: login_check to print "Login verified" and order_log to print "Order recorded". Apply both decorators to place_order() and display "Order placed successfully" from the original function.

# def dec1(func):
#     def wrap1(*args,**kwargs):
#         print("Login verified")
#         func(*args,**kwargs)
#     return wrap1
# def dec2(func):
#     def wrap2(*args,**kwargs):
#         func(*args,**kwargs)
#         print("order recorded")
#     return wrap2
# def place_order(username):
#     print("order placed successfully by",username)
# place_order=dec2(place_order)
# place_order=dec1(place_order)
# place_order("mohanavarshithak")




