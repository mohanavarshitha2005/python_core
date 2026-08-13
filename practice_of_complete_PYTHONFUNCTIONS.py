# SECTION 1 - DEFINING FUNCTIONS
# Q1.  Write a function called say_hello() that prints 'Welcome to Python!'

# say_hello=lambda x='welcome to python':x
# print(say_hello())

# Q2.  Write a function called add(a, b) that returns the sum of two numbers.

# add=lambda x,y:x+y
# print(add(2,3))

# Q4.  Write a function area_of_rectangle(length, width) that returns length * width. Call it with values 6 and 4.

# s=lambda len,bred:len*bred
# print(s(2,3))

# SECTION 2 - PARAMETERS

# Q1.  Write a function multiply(a, b, c) that returns the product of three numbers.

# m=lambda x,y,z:x*y*z
# print(m(2,3,2))

# Q2.  Create a function describe_pet(animal, name) that prints: 'My [animal] is named [name].'

# pet=lambda x,y:"my " + x + " " + "is named as" + " " + y
# print(pet('dog','lucky'))

# Q4.  Write a function power(base, exponent) that returns base raised to exponent using the ** operator.

# p=lambda x,y:x**y
# print(p(2,3))

# Q5.  Create a function full_name(first, middle, last) that returns the full name as a single string.

# name=lambda f,m,l:f + " " + m + " " + l
# print(name('kommineni','venkata','mohana varshitha'))

# SECTION 3 - POSITIONAL ARGUMENTS

# Q1.  Write a function intro(name, city, hobby) that prints a sentence about a person. Call it in two different orders and observe the difference.

intro=lambda x,y,z:'my name is ' +x+ " "+'my village is '+ " "+y+" my hobbies are"+ " "+z
print(intro('mohana','kondapi','playing games'))

# Q2.  Create subtract(a, b) that returns a - b. What is the difference between subtract(10, 3) and subtract(3, 10)?

# sub=lambda x,y:x-y
# print(sub(3,10))
# print(sub(10,3))

# Q4.  Write a function bio(first_name, last_name, age) and call it correctly using positional arguments.

# bio=lambda f,l,a:f+" "+l+" "+" age is "+ a
# print(bio('kommineni','venkata mohana varshitha','20'))

# SECTION 4 - KEYWORD ARGUMENTS

# Q1.  Call the function send_email(to, subject, body) using keyword arguments in any order.

# email=lambda to,sub,b:"mail is sending to" + " " + to + " " + "subject is " + sub + " " + "body is " + b
# print(email(to="teju",b="appying leave for 2 days because of fewer.",sub="application of leave"))

# Q2.  Write a function create_profile(username, email, age) and call it using keyword arguments.

# profile=lambda u,e,a:'username is' + " " + 'email is' + " " + 'age is' + " " + str(a)
# print(profile(u='mohana',a=20,e='mohanavarshithak@gmail.com'))

# Q4.  Rewrite this call using keyword arguments: book_ticket('Alice', 'Delhi', 'Mumbai', 2)

# book=lambda n='alice',s='delhi',c='mumbai',t=2:{n,c,s,t}
# print(book(n='mohana',t=5,s='ap',c='ong'))

# SECTION 5 - DEFAULT PARAMETERS

# Q1.  Write a function power(base, exponent=2) that returns base^exponent. Test with one and two arguments.

# ab = lambda x,y = 2: x**y
# print(ab(2))

# Q2.  Create a function connect(host, port=3306, protocol='TCP') and call it with various combinations.

# x=lambda x,y='3306',z='TCP': x + y + z
# print(x('mohana','3350','SMTP'))

# Q4.  Write a function discount_price(price, discount=10) that returns the discounted price. Test with and without the discount argument.

# dis_price=lambda p,d=10:p-(p*d/100)
# print(dis_price(3000))
# print(dis_price(3500,20))

# SECTION 6 - *ARGS AND **KWARGS

# Q1.  Write a function multiply_all(*args) that returns the product of all numbers passed.

# from functools import reduce
# mul=lambda *args:reduce(lambda x,y:x*y,args)
# print(mul(2,3,4))

# Q2.  Create a function display_tags(**kwargs) that prints each keyword-value pair on its own line.

# tags=lambda **x:x
# print(tags(name='mohana',age=20))

# Q3.  Write a function describe_person(name, *hobbies) where name is a regular param and hobbies are collected into a tuple.

# person=lambda n,*h:{'name':n,'hobbies':h}
# print(person('mohana','playing','reading','writing'))

# Q4.  What is the output of: def f(*args): print(type(args))  →  f(1, 2, 3)? Explain why.

# t=lambda *x:type(x)
# print(t(1,2,3,4,5))

# Q5.  Write a function create_html_tag(tag, **attributes) that prints: <tag key='val' ...>. Example: create_html_tag('a', href='https://python.org', target='_blank')

# tag=lambda t,**a:("<" + t + " ".join(f'{k}={v}' for k,v in a.items())+">")
# print(tag(t='a',href='httpslogin',color='blue'))

# Q6.  Write a function mixed(a, b, *args, **kwargs) and call it with at least 6 arguments. Print each part.

# mixed=lambda x,y,*args,**kwargs:(x,y,args,kwargs)
# print(mixed(10,20,30,39,40,56,name='mohana',age=20,score=90))

# SECTION 7 - FUNCTIONAL REFERENCES

# Q1.  Assign the built-in function len to a variable called count. Use it to find the length of a list.

# l=lambda x:len(x)
# print(l('mohana'))

# Q2.  Write a function run_twice(func, value) that calls func on value twice and returns the final result.

# func=lambda x:x**2
# twice=lambda x:func(func(x))
# print(twice(2))

# Q3.  Store the functions upper, lower, and title (string methods) in a dictionary. Let the user choose which one to apply.

# op={'upper':lambda x:x.upper(),
#     'lower':lambda x:x.lower(),
#     'title':lambda x:x.title()}
# print(op['upper']('mohana'))

# Q4.  Write a function that returns another function. Example: make_multiplier(3) should return a function that multiplies any number by 3.

# func=lambda x:x*3
# mul=lambda x:func(x)
# print(mul(3))

# SECTION 8 - LAMBDA

# Q1.  Write a lambda function that takes a number and returns its cube.

# c=lambda x:x**3
# print(c(2))

# Q2.  Create a lambda that takes two numbers and returns the larger one using a conditional expression (x if x > y else y).

# l=lambda x,y:x if x>y else y
# print(l(30,40))

# Q3.  Convert this regular function into a lambda: def even(n): return n % 2 == 0

# even=lambda x:x%2==0
# print(even(4))

# Q4.  Use a lambda with .sort() to sort this list of tuples by the second element: [(1,'banana'),(2,'apple'),(3,'cherry')]

# l=[1,6,5,4,8,10]
# l.sort(key=lambda x:x,reverse=True)
# print(l)

# l=[(1,'banana'),(2,'apple'),(3,'cherry')]
# l.sort(key=lambda x:x[1],reverse=False)
# print(l)

# l=[(1,'banana'),(2,'apple'),(3,'cherry')]
# lst=lambda x:sorted(l,key=lambda t:t[1],reverse=True)
# print(lst(l))

# SECTION 9 -HIGHER ORDER FUNCTIONS

# Q1.  Use map() to convert a list of temperatures in Celsius to Fahrenheit. Formula: F = (C × 9/5) + 32

# d=lambda x:(x*9/5)+32
# print(d(45))

# l=[45,76,87,34]
# print(list(map(lambda x:(x*9/5) + 32,l)))

# Q2.  Use filter() to extract all words from a list that start with a capital letter.

# l=['Hello','Hai','Gdmrng','amma']
# print(list(filter(lambda x:x==x.capitalize(),l)))

# Q3.  Use reduce() to find the product of all numbers in a list: [1, 2, 3, 4, 5] → 120

# from functools import reduce
# l=[1,2,3,4,5]
# print(reduce(lambda x,y:x*y,l))

# Q4.  Sort a list of tuples (name, age) by age in descending order using sorted() with a lambda key.

# l=[('mohana',90),('asha',78),('teju',85)]
# print(sorted(l,key=lambda x:x[1],reverse=True))

# Q5.  Chain map() and filter(): from [1..10], first filter out odds, then square the remaining evens.

# l=[1,2,3,4,5,6,7,8,9,10]
# print(list(map(lambda x:x**2,list(filter(lambda x:x%2==0,l)))))

# Q6.  Write your own version of map() called my_map(func, lst) using a regular loop. Verify it gives the same results as the built-in.

# l=[1,2,3,4,5,6,7,2,3,4]
# func=lambda x:x
# def my_map(func,lst):
#     res=[]
#     for i in lst:
#         res.append(i*2)
#     return res
# print(my_map(func,list(filter(lambda x:x%2==0,l))))

# Use reduce() to find the longest string in a list: ['cat', 'elephant', 'dog', 'rhinoceros']

# from functools import reduce
# l=['cat','elephant','dog','rhinoceros']
# print(reduce(lambda x,y:x if x>y else y,l))

# MIXED FUNCTIONS CHALLENGE

# Q1.  PARAMETERS + LAMBDA: Write a function apply_operation(a, b, op) where op is a lambda. Call it with operations for add, subtract, and multiply.

# op={'add':lambda x,y:x+y,
#     'sub':lambda x,y:x-y,
#     'mul':lambda x,y:x*y}
# def apply_operation(a,b,op):
#     return op(a,b)
# print(apply_operation(0,30,op['add']))

# Q3.  DEFAULT + KEYWORD + LAMBDA: Write a function make_greeting(name, prefix='Hello', formatter=lambda x: x) that applies formatter to the final greeting string. Test with str.upper as the formatter.

# def greeting(name,prefix='hello',formatter=lambda x:x):
#     return formatter(prefix + " " + name)
# print(greeting('mohana',formatter=lambda x:x.upper()))

# Q4.  map() + filter() + lambda: Given a list of integers from 1 to 20, use filter() to keep multiples of 3, then use map() to square them. Print the result.

# l=[1,2,3,4,5,6,7,81,2,3,5,6,89]
# print(list(map(lambda x:x**2,list(filter(lambda x:x%3==0,l)))))

# Q5.  FUNCTION REFERENCE + HIGHER ORDER: Create a list of lambda functions [double, triple, quadruple]. Write a function apply_all(funcs, value) that applies each in sequence and returns the final result.

# def apply_all(funcs,value):
#     res=[]
#     for i in funcs:
#         res.append(i(value))
#     return res
# func=[lambda x:x*2,
#       lambda x:x*3,
#       lambda x:x*4]
# print(apply_all(func,2))

# Q7.  **kwargs + reduce(): Write a function weighted_average(**scores) where keys are subjects and values are scores. Use reduce() to compute the average of all values.

# from functools import reduce
# def weighted_average(**scores):
#     res=[]
#     for key,value in scores.items():
#         res.append(value)
#     s=reduce(lambda x,y:x+y,res)
#     return s
# print((weighted_average(maths=90,sc=80,phy=75,ds=87)))

# Q8.  FULL PIPELINE: Build a mini data pipeline. Start with a list of student dictionaries [{name, score}]. Use filter() to keep scores >= 60, map() to add a 'grade' key ('Pass'), and sorted() to sort by score descending. Print the final result.

# l=[{'name':'mohana','score':90},
# {'name':'asha','score':78},
#    {'name':'teju','score':98}]
# print(sorted(list(map(lambda x:{**x ,'grade' : 'pass' if x['score']>=60 else 'fail'},list(filter(lambda x:x['score']>=60,l)))),key=lambda x:x['score'],reverse=True))

# Q9.  LAMBDA + sorted() + FUNCTION REFERENCE: Store three sort strategies in a dictionary: by_name, by_score, by_length. Let the user choose a strategy by name, then apply it to sort a list of tuples.

# s={'by_name':lambda x:sorted(l,key=lambda t:t[0],reverse=True),
#    'by_score':lambda x:sorted(l,key=lambda t:t[1],reverse=True),
#    'by_length':lambda x:sorted(l,key=lambda t:len(t[0]),reverse=True)
#    }
# l=[('mohana',80),('teju',78),('hyna',85),('balu',76)]
# print(s['by_name'](l))

# Q10.  ALL CONCEPTS: Write a function calculator(*args, operation='add', **options) that: (a) uses *args to collect numbers, (b) uses a default 'add' operation, (c) supports operations: 'add', 'multiply', 'max', 'min' using a dict of lambda functions, (d) if options contains show_steps=True, prints each step of the calculation.

# def calculator(*args,operation='add',**options):
#     res=args[0]
#     func=op[operation]
#     for i in args:
#         if options.get('show_steps'):
#              print(res,i,operation,func(res,i))
#         res=func(res,i)
#     return res
# op={'add':lambda x,y:x+y,
#     'mul':lambda x,y:x*y,
#     'max':lambda x,y:x if x>y else y,
#     'min':lambda x,y:x if x<y else y}
# print(calculator(1,2,3,4,5,6,operation='add',show_steps=True))



# Q1. Given a list of tuples (name, marks), sort the list:
#     * first by marks (descending)
#     * then by name (ascending)

# l=[('mohana',60),('asha',78),('teju',98),('vasavi',50)]
# l1=sorted(l,key=lambda x:x[1],reverse=True)
# print(sorted(l1,key=lambda x:x[0],reverse=False))

# Q2. Given a list of strings, sort them based on:
#     * length of string
#     * and then alphabetically

# l=['mohana','asha','teju','vasavi']
# print(sorted(l,key=lambda x:(len(x),x),reverse=True))

# 3. Given a list of integers, filter numbers divisible by both 2 and 5, add 5 to each using map(), then find the product using reduce().

# from functools import reduce
# l=[1,2,3,4,5,6,7,8,9,10,20]
# print(reduce(lambda x,y:x*y,list(map(lambda x:x+5,list(filter(lambda x:x%2==0 and x%5==0,l))))))

# Q3. Given a list of integers, write a program to:
# * Filter numbers divisible by 2 but not by 4
# * Add 3 to each using map()
# * Sort the result in descending order
# * Find the product of all elements using reduce().

# from functools import reduce
# l=[2,3,45,6,7,8,3]
# print(reduce(lambda x,y:x*y,sorted(list(map(lambda x:x+3,list(filter(lambda x:x%2==0 and x%4!=0,l)))),key=lambda x:x,reverse=True)))

# Q4. Given a list of words:
# * Filter words that start and end with the same letter
# * Convert them to lowercase
# * Sort by last character, then length
# * Join all words into a single string using reduce()

# from functools import reduce
# l=['mohanam','teju','asha','vasav','hynh']
# print(reduce(lambda x,y:x+y,sorted(list(map(lambda x:x.lower(),list(filter(lambda x:x[0]==x[-1],l)))),key=lambda x:(x[-1],len(x)),reverse=True)))

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
# print(reduce(lambda x,y:x+y,sorted(map(lambda x:x['amount']*1.05,filter(lambda x:x['type']=='credit',transactions)),reverse=True)))
#

# calculated both debit + credit

# from functools import reduce
# transactions = [
#     {"type": "credit", "amount": 1000},
#     {"type": "debit", "amount": 500},
#     {"type": "credit", "amount": 2000}
# ]
# print(reduce(lambda x,y:x+y,list(map(lambda x:x['amount'],filter(lambda x:x['type']=='debit',transactions))) + sorted(map(lambda x:x['amount']*1.05,filter(lambda x:x['type']=='credit',transactions)),reverse=True)))



# 1.Given a list of product prices, write a program to filter prices above ₹500, then apply a 10% discount using map(), and compute the final total bill using reduce().

# from functools import reduce
# l=[500,600,400,800,900]
# print(reduce(lambda x,y:x+y,list(map(lambda x:x-(x*0.1),list(filter(lambda x:x>500,l))))))

# 2. Given a list of numbers, write a program to filter negative numbers, then convert them into positive numbers using map(), and find their sum using reduce().

# from functools import reduce
# l=[-1,-2,-3,-5,6,7,-4,-8,4]
# print(reduce(lambda x,y:x+y,list(map(lambda x:-x,list(filter(lambda x:x<0,l))))))

# 3.Given a list of integers, write a program to filter numbers less than 50, then multiply each by 3 using map(), and determine the maximum value using reduce().

# from functools import reduce
# l=[50,100,150,51,65,45,23,45,1500]
# print(reduce(lambda x,y:x if x>y else y,list(map(lambda x:x*3,list(filter(lambda x:x<50,l))))))

# 4.Given a list of words, write a program to filter words with length greater than 3, then convert them to uppercase using map(), and concatenate them into a single string using reduce().

# from functools import reduce
# l=['amma','nanna','hi','hello','gd','oo','byee']
# print(reduce(lambda x,y:x+y,list(map(lambda x:x.upper(),list(filter(lambda x:len(x)>3,l))))))

# 5.A company tracks employee salaries. Write a program to filter salaries greater than ₹30,000, increase them by 15% using map(), and compute the total salary expenditure using reduce().

# from functools import reduce
# l=[31000,40000,50000,35000,60000]
# print(reduce(lambda x,y:x+y,list(filter(lambda x:x<=30000,l))+list(map(lambda x:x+(x*0.15),list(filter(lambda x:x>30000,l))))))

# 6.A data analysis system stores a list of integers. Write a program to filter odd numbers, square each using map(), and compute their sum using reduce().

# from functools import reduce
# l=[1,2,3,4,5,6,7,8,9,10]
# print(reduce(lambda x,y:x+y,list(map(lambda x:x**2,list(filter(lambda x:x%2==1,l))))))

# 7.An e-commerce platform stores product prices in a list. Write a program to filter products priced above ₹500, apply a 10% discount to those products using map(), and then calculate the total bill amount using reduce().

# from functools import reduce
# l=[500,600,400,800,900]
# print(reduce(lambda x,y:x+y,list(filter(lambda x:x<=500,l))+list(map(lambda x:x-(x*0.1),list(filter(lambda x:x>500,l))))))

# 8.A banking system stores transaction amounts. Write a program to filter only credit transactions (positive values), apply a processing bonus of ₹10 to each using map(), and calculate the total credited amount using reduce().

# from functools import reduce
# l=[-1,-2,-3,-5,6,7,-4,-8,4]
# print(reduce(lambda x,y:x+y,list(map(lambda x:x+10,list(filter(lambda x:x>0,l))))))



# 1.Given a list of integers, write a program to filter even numbers and then multiply each of them by 3 using a single pipeline.

# l=[1,2,3,4,5,6,7,8]
# print(list(map(lambda x:x+3,list(filter(lambda x :x%2==0,l)))))

# 2.Given a list of numbers, write a program to filter numbers greater than 20 and then square each of the filtered numbers using map().

# l=[10,20,30,21,40,50]
# print(list(map(lambda x:x**2,list(filter(lambda x:x>20,l)))))

# 3. Given a list of words, write a program to filter words whose length is greater than 4 and then convert those words into uppercase using a single pipeline.

# l=['amma','mohana','hiiiq','tejasri','sussela','srilakshmi']
# print(list(map(lambda x:x.upper(),list(filter(lambda x:len(x)>4,l)))))

# 4.Given a list of integers, write a program to filter numbers divisible by 5 and then add 10 to each of the filtered numbers.

# l=[2,3,4,5,6,10,15,76,65,76,89,100,45]
# print(list(map(lambda x:x+10,list(filter(lambda x:x%5==0,l)))))

# 5. Given a list of student marks, write a program to filter students who scored more than 40 and then increase their marks by 5 using map()

# l=[{'name':'mohana','score':40},
#    {'name':'asha','score':80},
# {'name':'teju','score':90},
# {'name':'vasavi','score':45}]
# print(list(map(lambda x:{**x,'score':x['score']+10},list(filter(lambda x:x['score']>40,l)) )))

# 6. Given a list of strings, write a program using reduce() to concatenate all strings into a single string.

# from functools import reduce
# l=['amma','mohana','hiiiq','tejasri','sussela','srilakshmi']
# print(reduce(lambda x,y:x+y,l))

# 7. Given a list of digits, write a program using reduce() to form a single number (e.g., [1,2,3] → 123).

# from functools import reduce
# l=[1,2,3,4,5,6]
# print(reduce(lambda x,y:str(x)+str(y),l))

# 8. Given a list of numbers, write a program using reduce() to calculate the cumulative difference

# from functools import reduce
# l=[1,2,3,4,5,6]
# print(reduce(lambda x,y:x-y,l))

# 9. Given a list of student marks, write a program using reduce() to find the total marks and then compute the average.

# from functools import reduce
# l=[1,2,3,4,5,6,7,8,910]
# print(reduce(lambda x,y:x+y,l)/len(l))

# 10.  Given a list of product prices, write a program to:
#
# * Filter prices greater than ₹500
# * Apply a 10% discount to the filtered prices using map()

# l=[{'product':'mixi','price':700},
#    {'product':'fan','price':500},
#    {'product':'oven','price':900},
#    {'product':'ac','price':40000}]
# print(list(filter(lambda x:x['price']<=500,l))+list(map(lambda x:{**x,'price':x['price']-x['price']*0.1},list(filter(lambda x:x['price']>500,l)))))

# 1. An online store stores product prices in a list. Write a program using map() to apply a 10% tax to each product price and display the updated prices.

# l=[{'product':'mixi','price':700},
#    {'product':'fan','price':500},
#    {'product':'oven','price':900},
#    {'product':'ac','price':40000}]
# print(list(filter(lambda x:x['price']<=500,l))+list(map(lambda x:{**x,'price':x['price']+x['price']*0.1},l)))

# 2. A list of usernames is stored in lowercase. Use map() to format them so that the first letter is uppercase.

# l=['amma','mohana','hiiiq','tejasri','sussela','srilakshmi']
# print(list(map(lambda x:x.title(),l)))

# 3. An e-commerce website wants to display only products priced above ₹500. Use filter() to extract those prices from a list.

# l=[{'product':'mixi','price':700},
#    {'product':'fan','price':500},
#    {'product':'oven','price':900},
#    {'product':'ac','price':40000}]
# print(list(filter(lambda x:x['price']>500,l)))

# 4. Use map() with a lambda function to multiply each number in a list by 5.
#
# l=[1,2,3,4,5,6,7,8,9,10]
# print(list(map(lambda x:x*5,l)))

# 5. Write a program that uses map() to calculate the length of each word in a list of strings.

# l=['amma','mohana','hiiiq','tejasri','sussela','srilakshmi']
# print(list(map(lambda x:len(x),l)))

# 6. Given a list of integers, use filter() to select numbers greater than 50.

# l=[10,20,50,56,75,45,87,65,34,90,100]
# print(list(filter(lambda x:x>50,l)))

# 7. Use filter() with a lambda function to select numbers that are multiples of 4.

# l=[10,20,50,56,75,45,87,65,34,90,100]
# print(list(filter(lambda x:x%4==0,l)))

# Q1. Write a lambda to calculate simple interest.
# Formula: (P * R * T) / 100

# s=lambda p,t,r:(p*t*r)/100
# print(s(100000,2,3))

# Q2. Temperature Converter
# Write a lambda to convert Celsius to Fahrenheit.
# Formula: (C * 9/5) + 32

# d=lambda c:(c*9/5)+32
# print(d(34))

# Q3. Electricity Bill
# Write a lambda that calculates bill amount:
# * If units ≤ 100 → ₹5/unit
# * Else → ₹8/unit

# b=lambda x:x*8 if x>100 else x*5
# print(b(100))

# Q4. Login Check
# Write a lambda that checks if username equals "admin" and password equals "1234" and returns "Login Success" or "Invalid".

# l=lambda u,p:"Login Success" if u=='admin' and p=='1234' else "invalid"
# print(l('admin','1234'))


# 1. Write a function simple_interest(principal, rate=5, time=1) to calculate simple interest. Demonstrate different function calls by passing only required arguments and then overriding default values.

# s=lambda p,t,r:(p*t*r)/100
# print(s(100000,2,3))

# 2. Create a function student_info(name, *subjects, **details) that prints a student’s name, subjects enrolled, and additional details like grade and school.

# student=lambda n,*s,**d:{'name':n,"subjects enrolled":s,"additional details":d}
# print(student('mohana','ds','c','c++','java','python',school='bwec',grade='A'))

# 3. Write a function order_food(*items, **preferences) that accepts multiple food items and optional preferences like spice level or delivery time. Display the order summary.

# order=lambda *i,**p:{'ordered items':i,'preferences':p}
# print(order('fried rice','biryani','aavakai rice','burger','pizza','strawberry_icecream',spice='too_spicy',delivery_time='1:30 pm'))

# 4. Write a function shopping_cart(discount=0, *prices) that calculates the total price after applying a discount. Demonstrate calling the function with and without the discount argument.

# from functools import reduce
# t=lambda *p,d=0:reduce(lambda x,y:x+y-d,p)
# print(t(500,400,600,900,d=10))

# 5. Design a function register_user(username, role="user", *permissions, **details) that stores user information, including optional permissions and additional attributes.

# u=lambda u,r='user',*p,**d:{'username':u,'role':r,'permissions':p,'details':d}
# print(u('mohana','admin','too late','food free',city='hyd',age=20))

# 6.Write a program to create a list containing dictionaries. Perform a shallow copy and a deep copy of the list. Modify a value inside one of the dictionaries in the original list and display all lists. Explain the observed behavior.

# import copy
# l=[{'product':'mixi','price':700},
#    {'product':'fan','price':500},
#    {'product':'oven','price':900},
#    {'product':'ac','price':40000}]
# print(l)
# shallow_cpy=copy.copy(l)
# l[0]['price']=1000
# print(l)
# print(shallow_cpy)
# deep_cpy=copy.deepcopy(l)
# l[1]['product']='cooler'
# print(l)
# print(deep_cpy)

# 7. Define a function login(username, password="1234"). Demonstrate how default arguments work and explain a potential issue with using default passwords.

# l=lambda u,p='1234':{'username':u,'password':p}
# print(l('mohana'))
# print(l('mohana','52347'))

# 8. Write a function area(length, breadth=None) that calculates the area of a rectangle. If breadth is not provided, assume it is a square and compute accordingly.

# a=lambda l,b: l*l if b=='none' else l*b
# print(a(2,'none'))
# print(a(4,3))

# 9. Write a function calculate_score(base_score=0, *bonus_points, **penalties) that computes a final score after adding bonuses and subtracting penalties.

# from functools import reduce
# s=lambda bp,*b,**p:bp+reduce(lambda x,y:x+y,b)-reduce(lambda x,y:x+y,p.values())
# print(s(300000,4000,700,299,dis=40000,offer=5000))

# def calculate_score(bp=0,*b,**p):
#     sum=0
#     v=0
#     for i in b:
#         sum+=i
#     for value in p.values():
#         v+=value
#     return bp + sum - v
# print(calculate_score(300000,4000,700,299,dis=40000,offer=5000))

# 10. Design a function send_email(sender, receiver, subject="No Subject", *attachments, **options) that simulates sending an email with optional attachments and settings.

# email=lambda s,r,sub,*a,**options:s + " " + "sending mail to " + r +" subject is " + sub + " " + "attachments are " +  str(a) + " options are" + str(options)
# print(email('mohana','teju','taking a leave','letter of doctor appointment','video',age=20,ondate='20/8/26'))

# 1. Design a function where the applicant name is a positional argument and job role (“developer”) is a default argument. The function should accept multiple skills using *args and additional details like experience, location preference, and expected salary using **kwargs. Display application summary.

# a=lambda n,r='developer',*s,**e:"my name is " + n + " and role is " + r + " skills are " + str(s) + " and experiences are " + str(e)
# print(a('mohana','developer','python','java','html','css','dbms',wipro='2+ yeare',cognizant='4 years'))

# 1. Design a Python program for a supermarket billing system. Create a function calculate_total(prices) that accepts the prices of multiple items and returns their total cost. Then define a function apply_discount(*amount) that applies a 10% discount if the total exceeds 1500. Finally, create a function final_bill(*details) that accepts keyword arguments such as amount, tax, and packing_charge, and returns the final payable bill. Display the final amount using a single nested function call.

# def calculate_total(*prices):
#     sum=0
#     for i in prices:
#         sum+=i
#     return sum
# def apply_discount(amount):
#     if amount>1500:
#         return amount-(amount*0.1)
#     return amount
# def final_bill(**details):
#     f=0
#     for key ,value in details.items():
#         f+=value
#     return f
# print(final_bill(amount=apply_discount(calculate_total(1000,2000,3000)),tax=500,packing_charge=100))

# from functools import reduce
# calculate_total=lambda *prices:reduce(lambda x,y:x+y,prices)
# apply_discount=lambda amount:amount-(amount*0.1) if amount >1500 else amount
# final_bill=lambda **d:reduce(lambda x,y:x+y,d.values())
# print(final_bill(amount=apply_discount(calculate_total(1000,2000,3000)),tax=500,packing_charge=100))

# Write a Python program to simulate a Zomato-like food ordering system where a user can store their name, order ID, and delivery location using variables. Maintain a list of ordered food items, a set of restaurants to ensure no duplicates, and a dictionary to store order details such as total bill and order status. Demonstrate how adding items updates the list and how duplicate restaurants are handled.

# name='mohana'
# order_id='123456'
# delivery_location='hyd'
# ordered_items=['fried rice','biryani','burger','pizza']
# restuarants={'kb','nice','babai hotel','missamma','bhavpuri'}
# order_details={'total_bill':5000,'order_status':'confirmed'}
# print("zomato_like food ordering system")
# print(name)
# print(order_id)
# print(delivery_location)
# print(ordered_items)
# ordered_items.append('biryani')
# print(ordered_items)
# print(restuarants)
# restuarants.add('kb')
# restuarants.add('ismail')
# print(restuarants)
# print(order_details)
# order_details['total_bill']=6000
# print(order_details)

# Develop a Python application for a Flipkart-like shopping cart system where user details like name and customer ID are stored as immutable variables. Use a list to manage products added to the cart, a set to store unique brands, and a dictionary to maintain order summary including total price and delivery status. Show how modifying cart items differs from updating user details.

# name='mohana'
# order_id='123456'
# delivery_location='hyd'
# ordered_items=['fan','cooler','oven','chudidaar']
# brands={'vivo','apple','voltas','lg','samsung'}
# order_details={'total_bill':500000,'order_status':'confirmed'}
# print("flipcart_like shopping cart system")
# print(name)
# print(order_id)
# print(delivery_location)
# print(ordered_items)
# ordered_items.append('oven')
# ordered_items.append('washing machine')
# print(ordered_items)
# print(brands)
# brands.add('vivo')
# brands.add('redmi')
# print(brands)
# print(order_details)
# order_details['total_bill']=600000
# print(order_details)
