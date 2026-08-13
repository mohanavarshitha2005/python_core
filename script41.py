# Q1.  Write a function called say_hello() that prints 'Welcome to Python!'

# def say_hello():
#          print("welcome to python")
# say_hello()

# s=lambda : "welcome to python"
# print(s())

# Q2.  Write a function called add(a, b) that returns the sum of two numbers.

# def add(a,b):
#     return a+b
# print(add(2,3))

# a=lambda x,y:x+y
# print(a(2,3))

# Write a function area_of_rectangle(length, width) that returns length * width. Call it with values 6 and 4.

# def area_rectangle(len,breadth):
#     return len*breadth
# print(area_rectangle(2,3))

# a=lambda x,y:x*y
# print(a(2,3))

# SECTION 2 - PARAMETERS

# Write a function multiply(a, b, c) that returns the product of three numbers.

# def mul(a,b,c):
#     return a*b*c
# print(mul(2,3,4))

# m=lambda x,y,z:x*y*z
# print(m(2,3,4))

# Q2.  Create a function describe_pet(animal, name) that prints: 'My [animal] is named [name].'

# def pet(animal,name):
#     print('animal', animal,'name',name)
# pet('dog','lucky')

# p=lambda a,n:{'animal': a,'name':n}
# print(p('dog','lucky'))

# Q4.  Write a function power(base, exponent) that returns base raised to exponent using the ** operator.

# def power(base,exponent):
#     return base**exponent
# print(power(2,3))

# p=lambda x,y:x**y
# print(p(2,3))

# Q5.  Create a function full_name(first, middle, last) that returns the full name as a single string.

# def name(fi,mi,la):
#     return 'firstname',fi,'middlename',mi,'lastname',la
# print(name('kommineni','venkata','mohana varshitha'))

# n=lambda x,y,z:{'firstname':x,'middlename':y,'lastname':z}
# print(n('kommineni','venkata','mohana varshitha'))

# SECTION 3 - POSITIONAL ARGUMENTS

# Q1.  Write a function intro(name, city, hobby) that prints a sentence about a person. Call it in two different orders and observe the difference.

# def intro(name,city,hobby):
#     print("my name is",name,"city is",city,"hobby is",hobby)
# intro('mohana','ong','playing')

# introd=lambda x,y,z:"my name is "+ x + " city is " + y +" hobby is " + z
# print(introd('mohana','ong','playing'))

# Q2.  Create subtract(a, b) that returns a - b. What is the difference between subtract(10, 3) and subtract(3, 10)?

# def sub(a,b):
#     return a-b
# print(sub(3,10))
# print(sub(10,3))

# s=lambda x,y:x-y
# print(s(3,10))
# print(s(10,3))

# Q4.  Write a function bio(first_name, last_name, age) and call it correctly using positional arguments.

# def name(fi,mi,la):
#     return 'firstname',fi,'middlename',mi,'lastname',la
# print(name('kommineni','venkata','mohana varshitha'))

# n=lambda x,y,z:{'firstname':x,'middlename':y,'lastname':z}
# print(n('kommineni','venkata','mohana varshitha'))

# SECTION 4 - KEYWORD ARGUMENTS

# Q1.  Call the function send_email(to, subject, body) using keyword arguments in any order.

# def email(to,su,bo):
#     print('to',to,'su',su,'bo',bo)
# email(bo='leave due to fewer',to='teju',su='leave permission')

# e=lambda x,y,z:{'to':x,'su':y,'bo':z}
# print(e(z='leave due to fewer',x='teju',y='leave permission'))

# Q2.  Write a function create_profile(username, email, age) and call it using keyword arguments.

# def profile(us,em,ag):
#     print('username',us,'email',em,'age',ag)
# profile(em='mohanavarshithak@gmail.com',ag=20,us='mohana')

# p=lambda x,y,z:{'username':x,'email':y,'age':z}
# print(p(y='mohanavarshithak@gmail.com',z=20,x='mohana'))

# Q4.  Rewrite this call using keyword arguments: book_ticket('Alice', 'Delhi', 'Mumbai', 2)

# def book(na,ci,st,no):
#     print(na,ci,st,no)
# book('Alice', 'Delhi', 'Mumbai', 2)

# b=lambda x,y,w,z:x  + ' ' + y + ' ' + w + ' ' + str(z)
# print(b('Alice', 'Delhi', 'Mumbai', 2))

# SECTION 5 -DEFAULT PARAMETERS

# Write a function power(base, exponent=2) that returns base^exponent. Test with one and two arguments.

# def power(base,exponent=2):
#     return base**exponent
# print(power(2))

# p=lambda x,y=2:x**y
# print(p(2))

# Q2.  Create a function connect(host, port=3306, protocol='TCP') and call it with various combinations.

# def connect(host, port=3306, protocol='TCP'):
#     print(host,port,protocol)
# connect('mohana', port=3356, protocol='SMTP')
# connect('mohana')

# c=lambda x,y=3306,z='TCP':x + ' ' + str(y) + ' ' + z
# print(c('mohana', 3356, 'SMTP'))
# print(c('mohana'))

# Q4.  Write a function discount_price(price, discount=10) that returns the discounted price. Test with and without the discount argument.

# def price(p,d=10):
#     return p-(p*d/100)
# print(price(4000))
# print(price(4000,20))

# p=lambda x,y=10:x-(x*y/100)
# print(p(4000))
# print(p(4000,20))

# SECTION 6 - *ARGS AND **KWARGS

# Q1.  Write a function multiply_all(*args) that returns the product of all numbers passed.

# def mul(*args):
#     a=1
#     for i in args:
#         a*=i
#     return a
# print(mul(1,2,3,4,5,6,7,8))

# from functools import reduce
# m=lambda *x:reduce(lambda s,t:s*t,x)
# print(m(1,2,3,4,5,6,7,8))

# Q2.  Create a function display_tags(**kwargs) that prints each keyword-value pair on its own line.

# def tags(**kwargs):
#     print("<",end=" ")
#     for key,value in kwargs.items():
#         print(key,"=",value,end=" ")
#     print(">")
# tags(a_href='https//login.com',color='red')

# t=lambda **x:"<" + " ".join(f'{k}={v}' for k, v in x.items()) + ">"
# print(t(a_href='https//login.com',color='red'))

# Q3.  Write a function describe_person(name, *hobbies) where name is a regular param and hobbies are collected into a tuple.

# def person(name,*hobbies):
#     print("my name is ",name," and my hobbies are ",hobbies)
# person('mohana','playing','reading','writing')

# p=lambda x,*y:"my name is " + x + " and my hobbies are " + str(y)
# print(p('mohana','playing','reading','writing'))

# What is the output of:def f(*args): print(type(args))→ f(1, 2, 3)? Explain why.

# def f(*args):
#     print(type(args))
# f(1,2,3,4,5)

# fc=lambda *x:type(x)
# print(fc(1,2,3,4,5))

# Q5.  Write a function create_html_tag(tag, **attributes) that prints: <tag key='val' ...>. Example: create_html_tag('a', href='https://python.org', target='_blank')

# def tags(**kwargs):
#     print("<",end=" ")
#     for key,value in kwargs.items():
#         print(key,"=",value,end=" ")
#     print(">")
# tags(a_href='https//login.com',color='red')

# t=lambda **x:"<" + " ".join(f'{k}={v}' for k, v in x.items()) + ">"
# print(t(a_href='https//login.com',color='red'))

# Q6.  Write a function mixed(a, b, *args, **kwargs) and call it with at least 6 arguments. Print each part.

# def mixed(a,b,*args,**kwargs):
#     print(a, b, args, kwargs)
# mixed(10,20,1,2,3,4,5,n='mohana',age=20)

# m=lambda x,y,*w,**z:str(x) + ' ' + str(y)+ ' ' + str(w) + ' ' + str(z)
# print(m(10,20,1,2,3,4,5,n='mohana',a=20))

# SECTION 7 - FUNCTIONAL REFERNCES

# def le(a):
#     print(len(a))
# le('mohana')

# l=lambda x:len(x)
# print(l('mohana'))

# Q2.  Write a function run_twice(func, value) that calls func on value twice and returns the final result.

# def func(value):
#     return value**2
# def twice(func,value):
#     return func(func(value))
# print(twice(func,2))
#
# f=lambda x:x**2
# t=lambda func,v:func(func(v))
# print(t(f,2))

# Q3.  Store the functions upper, lower, and title (string methods) in a dictionary. Let the user choose which one to apply.

# def upper(y):
#     return y.upper()
# def lower(y):
#     return y.lower()
# def title(y):
#     return y.title()
# op={'upper':upper,
#     'lower':lower,
#     'title':title
#     }
# print(op['lower']('MOhana'))

# op={'upper':lambda x:x.upper(),
#     'lower':lambda x:x.lower(),
#     'title':lambda x:x.title()}
# print(op['lower']('MOhana'))

# Q4.  Write a function that returns another function. Example: make_multiplier(3) should return a function that multiplies any number by 3.

# def mul(v):
#     return v*3
# print(mul(9))

# m=lambda x:x*3
# print(m(9))

# SECTION 8 - LAMBDA

# Q1.  Write a lambda function that takes a number and returns its cube.

# c=lambda x:x**3
# print(c(3))

# Q2.  Create a lambda that takes two numbers and returns the larger one using a conditional expression (x if x > y else y).

# l=lambda x,y:x if x>y else y
# print(l(30,20))

# Q3.  Convert this regular function into a lambda: def even(n): return n % 2 == 0

# e=lambda x:x%2==0
# print(e(42))
# print(e(21))

# Q4.  Use a lambda with .sort() to sort this list of tuples by the second element: [(1,'banana'),(2,'apple'),(3,'cherry')]

# l=[(1,'banana'),(2,'apple'),(3,'cherry')]
# l.sort(key=lambda x:x[1],reverse=False)
# print(l)

# SECTION 9 - HIGHER-ORDER FUNCTIONS

# Q1.  Use map() to convert a list of temperatures in Celsius to Fahrenheit. Formula: F = (C × 9/5) + 32

# l=[32,43,56,78,90]
# print(list(map(lambda x:(x*9/5) + 32,l)))

# Q2.  Use filter() to extract all words from a list that start with a capital letter.

# l=['mohana','Teju','Asha','Vasavi']
# print(list(filter(lambda x:x==x.title(),l)))

# Q3.  Use reduce() to find the product of all numbers in a list: [1, 2, 3, 4, 5] → 120

# from functools import reduce
# l=[1,2,3,4,5]
# print(reduce(lambda x,y:x*y,l))

# Q4.  Sort a list of tuples (name, age) by age in descending order using sorted() with a lambda key.

# l=[('mohana',20),('teju',23),('vasavi',25),('asha',19)]
# print(sorted(l,key=lambda x:x[1],reverse=True))

# Q5.  Chain map() and filter(): from [1..10], first filter out odds, then square the remaining evens.

# l=[1,2,3,4,5,6,7,8,9,10]
# print(list(map(lambda x:x**2,list(filter(lambda x:x%2==0,l)))))

# Q6.  Write your own version of map() called my_map(func, lst) using a regular loop. Verify it gives the same results as the built-in.

# def my_map(func,lst):
#     res=[]
#     for i in lst:
#         res.append(i)
#     return res
# func=lambda x:x
# l=[1,2,3,4,5,6,7,8,9,10]
# print(my_map(func,l))

# Use reduce() to find the longest string in a list: ['cat', 'elephant', 'dog', 'rhinoceros']

# from functools import reduce
# l=['cat', 'elephant', 'dog', 'rhinoceros']
# print(reduce(lambda x,y:x if len(x)>len(y) else y,l))

# MIXED CONCEPT CHALLENGES

# Q1.  PARAMETERS + LAMBDA: Write a function apply_operation(a, b, op) where op is a lambda. Call it with operations for add, subtract, and multiply.

# def apply_operation(a,b,op):
#     return op(a,b)
# op={'add':lambda x,y:x+y,
#     'sub':lambda x,y:x-y,
#     'mul':lambda x,y:x*y}
# print(apply_operation(20,30,op['add']))

# Q3.  DEFAULT + KEYWORD + LAMBDA: Write a function make_greeting(name, prefix='Hello', formatter=lambda x: x) that applies formatter to the final greeting string. Test with str.upper as the formatter.

# def greet(n,p='Hello',formatter=lambda x:x):
#     return formatter(p + ' ' + n)
# print(greet('mohana',formatter=lambda x:x.upper()))

# Q4.  map() + filter() + lambda: Given a list of integers from 1 to 20, use filter() to keep multiples of 3, then use map() to square them. Print the result.

# l=[1,2,3,4,5,6,7,8,9,10]
# print(list(map(lambda x:x**2,list(filter(lambda x:x%2==0,l)))))

# Q5.  FUNCTION REFERENCE + HIGHER ORDER: Create a list of lambda functions [double, triple, quadruple]. Write a function apply_all(funcs, value) that applies each in sequence and returns the final result.

# def apply_all(func,value):
#     res=[]
#     for i in func:
#         res.append(i(value))
#     return res
# func=[lambda x:x*2,
#     lambda x:x*3,
#     lambda x:x*4]
# print(apply_all(func,2))

# Q7.  **kwargs + reduce(): Write a function weighted_average(**scores) where keys are subjects and values are scores. Use reduce() to compute the average of all values.

# from functools import reduce
# def ws(**scores):
#     res=[]
#     for key,value in scores.items():
#         res.append(value)
#     a=reduce(lambda x,y:x+y,res)/len(res)
#     return a
# print(ws(maths=90,science=80,ds=85,python=97,cc=90))

# Q8.  FULL PIPELINE: Build a mini data pipeline. Start with a list of student dictionaries [{name, score}]. Use filter() to keep scores >= 60, map() to add a 'grade' key ('Pass'), and sorted() to sort by score descending. Print the final result.

# l=[{'name':'mohana','score':90},
#    {'name':'teju','score':85},
#    {'name':'asha','score':80},
# {'name':'vasavi','score':98},]
# print(sorted(list(map(lambda x:{**x,'grade' : 'pass' if x['score']>=60 else fail},list(filter(lambda x:x['score']>=60,l)))),key=lambda x:x['score'],reverse=True))

# Q9.  LAMBDA + sorted() + FUNCTION REFERENCE: Store three sort strategies in a dictionary: by_name, by_score, by_length. Let the user choose a strategy by name, then apply it to sort a list of tuples.

# op={'by_name':lambda x:sorted(l,key=lambda t:t[0],reverse=True),
#     'by_score':lambda x:sorted(l,key=lambda t:t[1],reverse=True),
#     'by_length':lambda x:sorted(l,key=lambda t:len(t[0]),reverse=True)}
# l=[('mohana',20),('teju',23),('vasavi',25),('asha',19)]
# print(op['by_name'](l))
# print(op['by_score'](l))
# print(op['by_length'](l))

# Q10.  ALL CONCEPTS: Write a function calculator(*args, operation='add', **options) that: (a) uses *args to collect numbers, (b) uses a default 'add' operation, (c) supports operations: 'add', 'multiply', 'max', 'min' using a dict of lambda functions, (d) if options contains show_steps=True, prints each step of the calculation.

# def calculator(*args,operation='add',**options):
#     func=op[operation]
#     res=args[0]
#     for i in args[1:]:
#         if options.get('show_steps'):
#             print(res,i,operation,func(res,i))
#         res=func(res,i)
#     return res
# op={'add':lambda x,y:x+y,
#     'mul':lambda x,y:x*y,
#     'max':lambda x,y:x if x>y else y,
#     'min':lambda x,y: x if x<y else y}
# print(calculator(1,2,3,4,5,6,7,operation='add',show_steps=True))

# Design a Python program for a supermarket billing system. Create a function calculate_total(prices) that accepts the prices of multiple items and returns their total cost. Then define a function apply_discount(*amount) that applies a 10% discount if the total exceeds 1500. Finally, create a function final_bill(*details) that accepts keyword arguments such as amount, tax, and packing_charge, and returns the final payable bill. Display the final amount using a single nested function call.

# def calculate_total(**price):
#     sum=0
#     for key,value in price.items():
#         sum+=value
#     return sum
# def apply_discount(amount):
#     d=0
#     if amount >1500:
#         d=amount-amount*0.1
#     else:
#         d=amount
#     return d
# def final_bill(**details):
#     bill=0
#     for key,value in details.items():
#         bill+=value
#     return bill
# print(final_bill(amount=(apply_discount(calculate_total(fan=1000,dress=800,oven=1500,ac=2000))),packing_charges=100,tax=150))

# from functools import reduce
# calculate_total=lambda **p:reduce(lambda x,y:x+y,p.values())
# apply_discount=lambda x:x-(x*0.1) if x>1500 else x
# final_bill=lambda **d:reduce(lambda s,t:s+t,d.values())
# print(final_bill(amount=(apply_discount(calculate_total(fan=1000,dress=800,oven=1500,ac=2000))),packing_charges=100,tax=150))

# Design a function where the applicant name is a positional argument and job role (“developer”) is a default argument. The function should accept multiple skills using *args and additional details like experience, location preference, and expected salary using **kwargs. Display application summary.

# def applicant(n,r='developer',*args,**kwargs):
#     print(n,r,args,kwargs)
# applicant('mohana','developer','java','python','html','css','js',experience='2+ years in wipro , 4+ years in cognizant',location_prefernce='hyd,banglore')

# a=lambda n,r='developer',*s,**e:n + ' ' + r + ' ' + str(s) + ' ' + str(e) + ' '
# print(a('mohana','developer','java','python','html','css','js',experience='2+ years in wipro , 4+ years in cognizant',location_prefernce='hyd,banglore'))

# Write a function simple_interest(principal, rate=5, time=1) to calculate simple interest. Demonstrate different function calls by passing only required arguments and then overriding default values.

# def s(p,t,r):
#     return (p*t*r)/100
# print(s(10000,2,5))

# s=lambda p,t,r:(p*t*r)/100
# print(s(10000,2,5))

# Create a function student_info(name, *subjects, **details) that prints a student’s name, subjects enrolled, and additional details like grade and school.

# def s(n,*sub,**d):
#     return n + ' ' + str(sub) + ' ' + str(d)
# print(s('mohana','python','java','php',clg='BWEC',grade='A'))

# s=lambda n,*sub,**d:n + ' ' + str(sub) + ' ' + str(d)
# print(s('mohana','python','java','php',clg='BWEC',grade='A'))

# 3. Write a function order_food(*items, **preferences) that accepts multiple food items and optional preferences like spice level or delivery time. Display the order summary.

# def o(*i,**p):
#     return str(i) + ' ' + str(p)
# print(o('fried rice','biryani','pizza','burger',spice_level='too spicy',delivery_time='1:30 pm'))

# o=lambda *i,**p:str(i) + ' ' + str(p)
# print(o('fried rice','biryani','pizza','burger',spice_level='too spicy',delivery_time='1:30 pm'))

# Write a function shopping_cart(discount=0, *prices) that calculates the total price after applying a discount. Demonstrate calling the function with and without the discount argument.

# def c(d=0,*p):
#     sum=0
#     for i in p:
#         sum+=i
#     return sum-(sum*d/100)
# print(c(0,200,300,400,500))
# print(c(10,200,300,400,500))

# from functools import reduce
# c=lambda d,*p:reduce(lambda x,y:x+y,p)-reduce(lambda x,y:x+y,p)*d/100
# print(c(0,200,300,400,500))
# print(c(10,200,300,400,500))

# Design a function register_user(username, role="user", *permissions, **details) that stores user information, including optional permissions and additional attributes.

# def r(u,ro='user',*p,**d):
#     return u + ' ' + ro + ' ' + str(p) + ' ' + str(d)
# print(r('mohana','user','too late','free food',clg='BWEC',grade='A'))

# r=lambda u,ro,*p,**d:u + ' ' + ro + ' ' + str(p) + ' ' + str(d)
# print(r('mohana','user','too late','free food',clg='BWEC',grade='A'))

# import copy
# l=[[1,2,3],[4,5,6],[6,7,8]]
# print(l)
# shallow_cpy=copy.copy(l)
# l[0][1]=10
# print(l)
# print(shallow_cpy)
# deep_cpy=copy.deepcopy(l)
# l[1][0]=10
# print(l)
# print(deep_cpy)

# Define a function login(username, password="1234"). Demonstrate how default arguments work and explain a potential issue with using default passwords.

# def l(u,p='1234'):
#     if u==str:
#         print(u+ ' '+p)
#     else:
#         print('enter user')
# l('mohana')
# l('mohana',p='1234')

# l=lambda u,p='1234': u+ ' '+p if u==str else 'enter user'
# print(l('mohana'))
# print(l('mohana',p='1234'))

# Write a function area(length, breadth=None) that calculates the area of a rectangle. If breadth is not provided, assume it is a square and compute accordingly.

# def a(l,b='none'):
#     if b=='none':
#         return l*l
#     else:
#         return l*b
# print(a(2))
# print(a(2,3))

# a=lambda l,b='none':l*l if b=='none' else l*b
# print(a(2))
# print(a(2,3))

# Write a function calculate_score(base_score=0, *bonus_points, **penalties) that computes a final score after adding bonuses and subtracting penalties.

# def s(bs,*b,**p):
#     sum=0
#     v=0
#     for i in b:
#         sum+=i
#     for value in p.values():
#         v+=value
#     return sum + v -bs
# print(s(1000,200,300,400,700,900,1500,tax=150,charges=500))

# from functools import reduce
# s=lambda bs,*b,**p:int(reduce(lambda x,y:x+y,b)) + int(reduce(lambda x,y:x+y,p.values()))-bs
# print(s(1000,200,300,400,700,900,1500,tax=150,charges=500))

# Design a function send_email(sender, receiver, subject="No Subject", *attachments, **options) that simulates sending an email with optional attachments and settings.

# def e(s,r,sub='no subject',*a,**o):
#     return s + ' ' + r + ' ' + sub + ' ' + str(a) + ' ' + str(o)
# print(e('mohana','teju','no subject','photo','video',email='mohanavarshithak@gmail.com',age=25))

# e=lambda s,r,sub='no subject',*a,**o:s + ' ' + r + ' ' + sub + ' ' + str(a) + ' ' + str(o)
# print(e('mohana','teju','no subject','photo','video',email='mohanavarshithak@gmail.com',age=25))

# Q1. Write a lambda to calculate simple interest.
# Formula: (P * R * T) / 100

# s=lambda p,t,r:(p*t*r)/100
# print(s(100000,2,3))

# Q2. Temperature Converter
# Write a lambda to convert Celsius to Fahrenheit.
# Formula: (C * 9/5) + 32

# t=lambda d:(d*9/5)+32
# print(t(67))

# Q3. Electricity Bill
# Write a lambda that calculates bill amount:
# * If units ≤ 100 → ₹5/unit
# * Else → ₹8/unit

# e=lambda b:b*8 if b>100 else b*5
# print(e(200))

# Q4. Login Check
# Write a lambda that checks if username equals "admin" and password equals "1234" and returns "Login Success" or "Invalid".

# l=lambda u,p:'login success' if u=='admin' and p=='1234' else 'imvalid'
# print(l('admin','1234'))

# - An online store stores product prices in a list. Write a program using map() to apply a 10% tax to each product price and display the updated prices.

# l=[200,300,400,600,100,900]
# print(list(map(lambda x:x+(x*0.1),l)))

# A list of usernames is stored in lowercase. Use map() to format them so that the first letter is uppercase.

# l=['mohana','teju','asha','vasavi']
# print(list(map(lambda x:x.title(),l)))

# An e-commerce website wants to display only products priced above ₹500. Use filter() to extract those prices from a list.

# l=[500,600,700,400,800,100,1000,1500]
# print(list(filter(lambda x:x>500,l)))

# Use map() with a lambda function to multiply each number in a list by 5.

# l=[1,2,3,4,5,6,7,8]
# print(list(map(lambda x:x*5,l)))

# Write a program that uses map() to calculate the length of each word in a list of strings.

# l=['mohana','teju','asha','vasavi']
# print(list(map(lambda x:len(x),l)))

# Given a list of integers, use filter() to select numbers greater than 50.

# l=[20,50,67,89,100,89,56,43,45,54,65,36,43,23]
# print(list(filter(lambda x:x>50,l)))

# Use filter() with a lambda function to select numbers that are multiples of 4.

# l=[20,50,67,89,100,89,56,43,45,54,65,36,43,23]
# print(list(filter(lambda x:x%4==0,l)))

# Given a list of integers, write a program to filter even numbers and then multiply each of them by 3 using a single pipeline.

# l=[20,50,67,89,100,89,56,43,45,54,65,36,43,23]
# print(list(map(lambda x:x*3,list(filter(lambda x:x%2==0,l)))))

# Given a list of numbers, write a program to filter numbers greater than 20 and then square each of the filtered numbers using map().

# l=[20,50,67,89,100,89,56,43,45,54,65,36,43,23]
# print(list(map(lambda x:x**2,list(filter(lambda x:x>20,l)))))

# Given a list of words, write a program to filter words whose length is greater than 4 and then convert those words into uppercase using a single pipeline.

# l=['mohana','teju','asha','vasavi']
# print(list(map(lambda x:x.upper(),list(filter(lambda x:len(x)>4,l)))))

# Given a list of integers, write a program to filter numbers divisible by 5 and then add 10 to each of the filtered numbers.

# l=[20,50,67,89,100,89,56,43,45,54,65,36,43,23]
# print(list(map(lambda x:x+10,list(filter(lambda x:x%5==0,l)))))

# Given a list of student marks, write a program to filter students who scored more than 40 and then increase their marks by 5 using map()

# l=[20,50,67,89,100,89,56,43,45,54,65,36,43,23]
# print(list(map(lambda x:x+5,list(filter(lambda x:x>40,l)))))

# Given a list of strings, write a program using reduce() to concatenate all strings into a single string.

# from functools import reduce
# l=['mohana','teju','asha','vasavi']
# print(reduce(lambda x,y:x+y,l))

# Given a list of digits, write a program using reduce() to form a single number (e.g., [1,2,3] → 123).

# from functools import reduce
# l=[1,2,3,4,5,6]
# print(reduce(lambda x,y:str(x)+str(y),l))

# Given a list of numbers, write a program using reduce() to calculate the cumulative difference

# from functools import reduce
# l=[1,2,3,4,5,6]
# print(reduce(lambda x,y:x-y,l))

# Given a list of student marks, write a program using reduce() to find the total marks and then compute the average.

# from functools import reduce
# l=[1,2,3,4,5,6]
# print(reduce(lambda x,y:x+y,l)/len(l))

#   Given a list of product prices, write a program to:
# * Filter prices greater than ₹500
# * Apply a 10% discount to the filtered prices using map()

# l=[500,600,700,400,800,100,1000,1500]
# print(list(map(lambda x:x-(x*0.1),list(filter(lambda x:x>500,l)))))

# Given a list of product prices, write a program to filter prices above ₹500, then apply a 10% discount using map(), and compute the final total bill using reduce().

# from functools import reduce
# l=[500,600,700,400,800,100,1000,1500]
# print(reduce(lambda x,y:x+y,list(map(lambda x:x-(x*0.1),list(filter(lambda x:x>500,l))))))

# Given a list of numbers, write a program to filter negative numbers, then convert them into positive numbers using map(), and find their sum using reduce().

# from functools import reduce
# l=[-1,-2,-3,-4,-5,-6,9,8,7,10,-11]
# print(reduce(lambda x,y:x+y,list(map(lambda x:-x,list(filter(lambda x:x<0,l))))))

# 3. Given a list of integers, write a program to filter numbers less than 50, then multiply each by 3 using map(), and determine the maximum value using reduce().

# from functools import reduce
# l=[20,50,67,89,100,89,56,43,45,54,65,36,43,23]
# print(reduce(lambda x,y :x if x>y else y,list(map(lambda x:x*3,list(filter(lambda x:x>50,l))))))

# Given a list of words, write a program to filter words with length greater than 3, then convert them to uppercase using map(), and concatenate them into a single string using reduce().

# from functools import reduce
# l=['mohana','teju','asha','vasavi']
# print(reduce(lambda x,y:x+y,list(map(lambda x:x.upper(),list(filter(lambda x:len(x)>3,l))))))

# A company tracks employee salaries. Write a program to filter salaries greater than ₹30,000, increase them by 15% using map(), and compute the total salary expenditure using reduce().

# from functools import reduce
# l=[31000,3600,4000,4000,5000,6000]
# print(reduce(lambda x,y:x+y,(list(filter(lambda x:x<=30000,l)))+list(map(lambda x:x+(x*0.15),list(filter(lambda x:x<30000,l))))))

# A data analysis system stores a list of integers. Write a program to filter odd numbers, square each using map(), and compute their sum using reduce().

# from functools import reduce
# l=[1,2,3,4,5,6,7,8,9,10]
# print(reduce(lambda x,y:x+y,list(map(lambda x:x**2,list(filter(lambda x:x%2==1,l))))))

# An e-commerce platform stores product prices in a list. Write a program to filter products priced above ₹500, apply a 10% discount to those products using map(), and then calculate the total bill amount using reduce().

# from functools import reduce
# l=[3100,3600,400,400,500,600]
# print(reduce(lambda x,y:x+y,(list(filter(lambda x:x<=500,l)))+list(map(lambda x:x-(x*0.1),list(filter(lambda x:x>500,l))))))

# A banking system stores transaction amounts. Write a program to filter only credit transactions (positive values), apply a processing bonus of ₹10 to each using map(), and calculate the total credited amount using reduce().

# from functools import reduce
# l=[-1,-2,-3,-4,-5,-6,9,8,7,10,-11]
# print(reduce(lambda x,y:x+y,list(map(lambda x:x+10,list(filter(lambda x:x>0,l))))))

# Q1. Given a list of tuples (name, marks), sort the list:
#     * first by marks (descending)
#     * then by name (ascending)

# l=[('mohana',70),('teju',89),('asha',76),('vasavi',89)]
# print(sorted(l,key=lambda x:(x[1],x[0]),reverse=(True,False)))

# Q2. Given a list of strings, sort them based on:
#     * length of string
#     * and then alphabetically

# l=['mohana','teju','vasavi','asha','yesmitha']
# print(sorted(l,key=lambda x:(len(x),x),reverse=False))

# 3. Given a list of integers, filter numbers divisible by both 2 and 5, add 5 to each using map(), then find the product using reduce().

# from functools import reduce
# l=[1,2,3,4,5,6,7,8,9,10]
# print(reduce(lambda x,y:x*y,list(map(lambda x:x+5,list(filter(lambda x:x%2==0 and x%5==0,l))))))

# Q3. Given a list of integers, write a program to:
# * Filter numbers divisible by 2 but not by 4
# * Add 3 to each using map()
# * Sort the result in descending order
# * Find the product of all elements using reduce().

# from functools import reduce
# l=[1,2,3,4,5,6,7,8,9,10]
# print(reduce(lambda x,y:x*y,sorted(list(map(lambda x:x+3,list(filter(lambda x:x%2==0 and x%4!=0,l)))),key=lambda x:x,reverse=True)))

# Q4. Given a list of words:
# * Filter words that start and end with the same letter
# * Convert them to lowercase
# * Sort by last character, then length
# * Join all words into a single string using reduce()

# from functools import reduce
# l=['mohana','teju','asha','vasavi','amma','oho']
# print(reduce(lambda x,y:x+y,sorted(list(map(lambda x:x.lower(),list(filter(lambda x:x[-1]==x[0],l)))),key=lambda x:x,reverse=False)))

# Q5. Given a list of transactions where each transaction contains a type (credit or debit) and an amount, write a program to filter only the credit transactions, apply a 5% bonus to each transaction amount using map(), sort the updated transactions in descending order based on the amount, and finally compute the total credited amount using reduce().
# INPUT:
# transactions = [
#     {"type": "credit", "amount": 1000},
#     {"type": "debit", "amount": 500},
#     {"type": "credit", "amount": 2000}
# ]

# from functools import reduce
# transactions = [
#     {"type": "credit", "amount": 1000},
#     {"type": "debit", "amount": 500},
#     {"type": "credit", "amount": 2000}
# ]
# print(reduce(lambda x,y:x+y,list(map(lambda x:x['amount'],filter(lambda x:x['type']=='debit',transactions))) + sorted(list(map(lambda x:x['amount']*1.05,list(filter(lambda x :x['type']=='credit',transactions)))),key=lambda x:x,reverse=True)))













