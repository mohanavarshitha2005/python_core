# def food_delivery_system(name,order_type='regular',*args,**kwargs):
#     print('name',':',name,'order_type',':',order_type, 'items',':', *args,'details',':',**kwargs)
# food_delivery_system('mohana','dynamic','biryani','fried rice','chicken','pizza',address='kbhp',payment='online payment done',delivery='track status',discount='10%')



# def food_delivery_system(name, order_type='regular', *args, **kwargs):
#     print("Name:", name,"Order Type:", order_type,"Items:", *args,"Details:", kwargs)
# food_delivery_system('mohana','dynamic',['biryani',299,'fried rice',199,'chicken',500,'pizza',800],address='kbhp',payment='online payment done',delivery='track status',discount='10%')
#
#
# def swiggy(customer_name, order_type = "regular", *items, **details):
#     print("Hi !", customer_name)
#     print("order type :", order_type)
#     total_bill = 0
#     print("Your order details are:")
#     for item in items:
#         print(item[0], "Rs.", item[1])
#         total_bill += item[1]
#     print("Additional Details:")
#     for detail,about in details.items():
#         print(detail, ":", about)
#     print("Total Bill: Rs. ", total_bill)

# swiggy("Archana", "Swiggy One",
#        ["Burger", 250],["Fries", 99],["Chips", 59],
#        ["Cola", 79],
#        payment_mode = "UPI",
#        address = "Road no 1, KPHB",
#        add_ons= ["ketchup", "mustard"])

# swiggy("Sai", "Swiggy Black",
#        ['Chicken Biryani', 250],['cola', 79], ['Gulab Jamun', 99],
#        payment_mode = "UPI",
#        cooking_instructions = "Make it a bit spicy.",
#        address = "Road no 2, KPHB")

# def describe_person(name, *hobbies):
#     print("Hi ! My name is ", name)
#     print("My hobbies are : ", end = " ")
#     for hobby in hobbies:
#         print(hobby, end = " ")

# describe_person("Latha", "Reading Books", "Travelling to the Mountains", "singing")

# def f(*args):
#     print(type(args))
# f(10,20,30)



# def html_tags(tag, **attributes):
#     print("<", tag, end = " ")
#     for attribute in attributes:
#         print(attribute," = ", attributes[attribute], end = "    ")
#     print(">")
#
# html_tags("'a'", style = "italic bold", border = "2px black",
#           height = "100%", width = "100%" )



# def html_tags(tag, **attributes):
#     print("<", tag, end = " ")
#     for value in attributes:
#         print(value," = ", attributes[value], end = "    ")
#     print(">")
#
# html_tags("'a'", style = "italic bold", border = "2px black",
#           height = "100%", width = "100%" )






