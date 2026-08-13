# l=[1,4,2,8,7,6,5,4,99,8]
# print(list(map(lambda x:x*3,list(filter(lambda x:x%2==0,l)))))


# l=[1,4,21,8,7,6,5,44,99,8]
# print(list(map(lambda x:x**2,list(filter(lambda x:x>20,l)))))

# l=['hii','bye','hello','gdmrng']
# print(list(map(lambda x:x.upper(),list(filter(lambda x:len(x)>4,l)))))


# l=[1110,4,20,85,7,60,5,4,990,8]
# print(list(filter(lambda x:x+10,list(map(lambda x:x%5==0,l)))))


# l=[30,20,54,34,45,23,56]
# print(list(map(lambda x:x+5,list(filter(lambda x :x>40,l)))))

# from functools import reduce
# l=['hii','bye','hello','gdmrng']
# print(reduce(lambda x,y:x+y,l))


# from functools import reduce
# l=[1,2,3,5,6,7,8]
# print(reduce(lambda x,y:str(x)+str(y),l))


# from functools import reduce
# l=[120,110,330,40,60,80,100,90]
# print(reduce(lambda x,y:x-y,l))


# from functools import reduce
# l=[30,40,60]
# x=(lambda x,y:x+y,l)
# print(reduce())
# c=(lambda x:count(x),l)
# print(c)
# print(reduce(lambda x,c:x//c,l))

# from functools import reduce
# l=[30,40,60]
# print(reduce(lambda x,y:x+y,l)/len(l))

l=[120,200,550,600,560,900,1000]
print(list(map(lambda x:x-(x*0.1),list(filter(lambda x: x>500,l)))))