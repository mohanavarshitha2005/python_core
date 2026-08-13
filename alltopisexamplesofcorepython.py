# def simple_interest(principal,rate=5,time=1):
#     return (principal*rate*time)/100
# print(simple_interest(10000))
# print(simple_interest(10000,6,2))


# def student_info(name,*subjects,**details):
#     print(name)
#     for i in subjects:
#         print(i)
#     for key,value in details.items():
#         print(key,":",value)
# student_info("mohana","python","java","wt",phno=6305078936,age=20,fathername="rama krishna")


# def order_food(*items,**preferences):
#     for i in items:
#         print(i)
#     for key,value in preferences.items():
#         print(key,";",value)
# order_food('fried rice','biryani','cool cake','noodles','burger')
# print()
# order_food('fried rice','biryani','cool cake','noodles','burger',spice_level="too spic",delivery_time="3:00 pm")


# def shopping_cart(discount=0,*prices):
#     t=0
#     for i in prices:
#         t=t+i
#     t=t-discount
#     print("price",":",t)
# shopping_cart(5000,10000,4000,3000,2000)


# def register_user(username,role="user",*permissions,**details):
#     print(username)
#     for i in permissions:
#         print(i)
#     for key,value in details.items():
#         print(key,";",value)
# register_user("mohana","too late","sick leave",phno=6305076438,fathername="rama krishna")
# print()
# register_user("mohana","too late","sick leave",phno=6305076438,fathername="ramakrishna")


import copy
list=[{age:20,name:"mohana"},{name:"vasavi",}]
print("hi")