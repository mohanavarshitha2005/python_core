# def power(base,exponent=2):
#     return base**exponent
# print(power(2,3))
#
#
# def connect(host,port=3306,protocol='TCP'):
#     print(host,port,'from',protocol)
# connect('mohana')
# connect('mohana',33986,'SMTP')
#
#
# def discount_price(price,discount=10):
#     return price-discount
# print(discount_price(3000))
# print(discount_price(3000,500))
#
#
# def multiply(*args):
#     a=1
#     for i in args:
#         a*=i
#     return a
# print(multiply(3,2,4))
#
#
# def display_tags(**kwargs):
#     for key,value in kwargs.items():
#         print(key,':',value)
# display_tags(name='mohana',age=20,marks=90)
#
#
# def calculate_total(**prices):
#     res = 0
#     for key,value in prices.items():
#         res=res+value
#     return res
# def apply_discount(*amount):
#     tot=0
#     for i in amount:
#         tot=tot+i
#     if tot>1500:
#         tot=tot-(tot*0.1)
#     return tot
# def final_bill(**details):
#     s=0
#     for key,value in details.items():
#         s+=value
#     return s
# print(final_bill(amount=apply_discount(calculate_total(saree=1550,dress=1540,chudidaar=2000)),tax=100,packing_charge=50))
#
#
# def describe_person(name,*hobbies):
#         print(name,'my hobbies are',hobbies)
# describe_person('mohana','playing','drawing','singing')
#
#
# def f(*args):
#     print(type(args))
# f(1,2,3,4)
#
#
# def create_html_tag(tag,**attributes):
#       print("<", tag, end=" ")
#       for key,value in attributes.items():
#            print(key,":",value,end=" ")
#       print(">")
# create_html_tag('a',href='hhtps://python.org',target='_blank')
#
#
# def mixed(a,b,*args,**kwargs):
#     print(a,b)
#     for i in args:
#         print(i,end=" ")
#     for key,value in kwargs.items():
#         print(key,":",value)
# mixed(6,5,10,3,24,35,17,18,age=20,name='mohana',score=90)
#
#
# l=[2,3,4,5,6]
# print(len(l))
#
# def square(a):
#     return a**2
# def cube(a):
#     return a**3
# def run_twice(func,value):
#     return func(func(value))
# print(run_twice(square,3))
#
#
# def add(a,b):
#     return a+b
# def sub(a,b):
#     return a-b
# def mul(a,b):
#     return a*b
# def div(a,b):
#     return a/b
# opp=input()
# op={'+':add,
#     '-':sub,
#     '*':mul,
#     '/':div
#     }
# print(op[opp](30,40))
#
#
# def upper(a):
#     return a.upper()
# def lower(a):
#     return a.lower()
# def title(a):
#     return a.title()
# op=input()
# opp={'+':upper,
#      '-':lower,
#      '*':title}
# print(opp[op]('helloworld'))
#
#
# def multiplier(a):
#     return a*3
# print(multiplier(10))
#
#
# def simple_interest(principal,rate=5,time=1):
#     return (principal*rate*time)/100
# print(simple_interest(10000))
#
#
# def student_info(name,*subjects,**details):
#     print(name,"subjects that she enrolled is",end=" ")
#     for i in subjects:
#         print(i,end=" ")
#     print("and additional details are",end=" ")
#     for key,value in details.items():
#         print(key,":",value,end=" ")
# student_info('mohana','java','python','c++','sql',age=20,language='english',native='ong',clg='BWEC')
#
#
# def order_food(*items,**preferences):
#     print("ordered food items are ",end=" ")
#     for i in items:
#         print(i,end=" ")
#     print("and they preferd that ",end=" ")
#     for key,value in preferences.items():
#         print(key,":",value,end=" ")
# order_food('fried rice','biryani','aavakai rice','ice cream',spicy='too less',delivery_time='1:30 pm')
#
#
#
# def shopping_cart(discount=0,*prices):
#     res=0
#     for i in prices:
#         res+=i
#     return res-discount
# print(shopping_cart(1000,2000,5000,4000,15000))
#
#
#
# def register_user(username,role='user',*permissions,**details):
#     print(username,"and the ","role is",role,"and the permissions are")
#     for i in permissions:
#         print(i)
#     print("and the details are")
#     for key,value in details.items():
#         print(key,":",value)
# register_user('mohana','user','by late to login','free for all works',pwd='1234',age=20)
#
#
# import copy
# l=[[2,3,4,5],[4,5,6,7]]
# shallow_cpy=copy.copy(l)
# print(shallow_cpy)
# print(l)
# l[0][1]=9
# print(shallow_cpy)
# print(l)
# deep_cpy=copy.deepcopy(l)
# l[1][0]=10
# print(l)
# print(deep_cpy)
#
#
# def login(username,pwd='1234'):
#     print(username,"you logined successfully!","and pwd is",pwd)
# login('mohana')
# login('mohana','234509')
# login(pwd="23456")
#
#
# def area(length,breadth='None'):
#     if breadth=='None':
#         return 4*length
#     else:
#         return length*breadth
# print(area(4,3))
# print(area(4))
#
#
# def calculate_score(base_score=0,*bonus_points,**penalities):
#     sum=0
#     for i in bonus_points:
#         sum+=i
#     s=0
#     for key,value in penalities.items():
#         s+=value
#     return base_score+sum-s
# print(calculate_score(10,3,5,6,10,16,ball=9,bat=4,wickets=4))
#
#
#
# def send_email(sender,reciever,subject="No Subject",*attachments,**options):
#     print(sender,'sended mail to',reciever,' and the subject is',subject,'and attachments are')
#     for i in attachments:
#         print(i)
#     print("and the settings are",end=" ")
#     for key,value in options.items():
#         print(key,":",value)
# send_email('mohana','vasavi','No Subject','audio','video','photos','offer letter',settings='quality')
#
#
#
# def cube(a):
#     return a**3
# print(cube(2))

# a=lambda x:x**3
# print(a(2))

# b=lambda x,y:x if x>y else y
# print(b(20,30))
# print(b(40,20))

#
# a=lambda x:x%2==0
# print(a(10))
# print(a(13))
#
#
# l=[(1,'banana'),(2,'apple'),(3,'cherry')]
# s=l.sort(key=lambda x:x[1])
# print(l)
#
#
# a=lambda x,y,z:(x*y*z)/100
# print(a(10000,2,1))


b=lambda x:(x*9/5)+32
print(b(40))


a=lambda x:x*5 if x<=100 else x*8
print(a(120))

b=lambda username,password:"login success" if username=='admin' and password=='1234' else "Invalid"
print(b(username='admin',password='1234'))






