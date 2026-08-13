# l=[1000,20000,300,5000]
# a=list(map(lambda x:x*1.1,l))
# print(a)

# l=['hello','hii','bye','gdii']
# a=list(map(lambda x:x.upper(),l))
# print(a)
#
# l=[100,20000,300,5000]
# a=list(filter(lambda x:x>500,l))
# print(a)


# l=[1000,20000,300,5000]
# a=list(map(lambda x:x*5,l))
# print(a)


# l=['hello','hii','bye','gdii']
# a=list(map(lambda x:len(x),l))
# print(a)


# l=[100,20,30,50,200]
# a=list(filter(lambda x:x>50,l))
# print(a)


# l=[100,20,30,50,200]
# a=list(filter(lambda x:x%4==0,l))
# print(a)

# EXPLAINED BY MAM FOR ALL EXAMPLES

# prices = [100,250,500,670,345,899]
def add_tax(price):
    return price * 1.1
# final_prices = list(map(add_tax, prices))
# print(list(map(lambda x : x * 1.1, prices)))
# print(final_prices)
# print(list(filter(lambda x : x > 500, prices)))
# print(list(map(lambda x : x * 5, prices)))

usernames = ["jude", "harry", "alice", "vini"]
# print(list(map(lambda x : x.title(), usernames)))
# print(list(map(lambda x : len(x), usernames)))

numbers = [1,2,3,45,67,56,89,23,1, 8, 0, 234, 123, 32 ,90, 16, 8, 4]
# print(list(filter(lambda x : x > 50, numbers)))
# print(list(filter(lambda x : x % 4 == 0, numbers)))