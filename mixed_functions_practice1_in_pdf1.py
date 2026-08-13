# def apply_operation(a,b,op):
#     return op(a,b)
# op={"add":lambda x,y:x+y,
#     "sub":lambda x,y:x-y,
#     "mul":lambda x,y:x*y}
# a=int(input())
# b=int(input())
# print(apply_operation(a,b,op["add"]))
# print(apply_operation(a,b,op["sub"]))
# print(apply_operation(a,b,op["mul"]))


# def make_greeting(name,prefix="hello",formatter=lambda x:x):
#     return formatter(prefix + " " + name)
# print(make_greeting('mohana',formatter=lambda x:x.upper()))


# l=[1,2,3,4,5,6,7,8,9,10]
# print(list(map(lambda x:x**2,list(filter(lambda x:x%3==0,l)))))


# funcs=[lambda x:2*x,
#       lambda x:3*x,
#       lambda x:4*x]
# def apply_all(funcs,value):
#     res=[]
#     for func in funcs:
#         res.append(func(value))
#     print(res)
# apply_all(funcs,3)


# funcs=[lambda x:2*x,
#       lambda x:3*x,
#       lambda x:4*x]
# def apply_all(funcs,value):
#     for func in funcs:
#         print(func(value))
# apply_all(funcs,3)


# from functools import reduce
# def weighted_scores(**scores):
#     res=[]
#     for key,value in scores.items():
#         res.append(value)
#     sum=reduce(lambda x,y:x+y,res)
#     c=len(res)
#     avg=sum/c
#     return avg
# print(weighted_scores(maths=90,science=80,python=60))


# l=[{'name':'mohana','score':60},
#    {'name':'asha','score':90},
#    {'name':'vasavi','score':85}]
# print(sorted(list(map(lambda x:{**x,'grade' : "pass" if x['score']>=60 else "fail"},list(filter(lambda x:x['score']>=60,l)))),key=lambda x:x['score'],reverse=True))


# l=[('mohana',60),('teju',80),('asha',90),('vasavi',85)]
# d = {
#     'by_name': lambda x: sorted(x, key=lambda t: t[0], reverse=True),
#     'by_score': lambda x: sorted(x, key=lambda t: t[1], reverse=True),
#     'by_length': lambda x: sorted(x, key=lambda t: len(t[0]), reverse=True)
# }
# def sort(c):
#    return d[c](l)
# print(sort('by_name'))


# def calculator(*args,operation='add',**options):
#     op = {'add': lambda x, y: x + y,
#           'multiply': lambda x, y: x * y,
#           'max': lambda x, y: x if x > y else y,
#           'min': lambda x, y: x if x < y else y}
#     func = op[operation]
#     res=args[0]
#     for i in args[1:]:
#         if options.get('show_steps'):
#             print(res,i,operation,func(res,i))
#         res=func(res,i)
#     print(res)
# calculator(1,2,3,4,5,6,7,2,3,9,10,operation='add',show_steps=True)
# calculator(1,2,3,4,5,6,7,2,3,9,10,operation='multiply',show_steps=True)
# calculator(1,2,3,4,5,6,7,2,3,9,10,operation='max',show_steps=True)
# calculator(1,2,3,4,5,6,7,2,3,9,10,operation='min',show_steps=True)

# func=lambda x:x*2
# def my_map(func,lst):
#     res=[]
#     for i in lst:
#         res.append(func(i))
#     return res
# l=[1,2,3,4,5,5,6,7,8]
# print(my_map(func,list(filter(lambda x:x%2==0,l))))


# def greet(name,prefix="Hello",formatter=lambda x:x):
#     return formatter(name + " " + prefix)
# print(greet('mohana',formatter=lambda x:x.upper()))


# l=[('mohana',60),('asha',80),("yesmitha",100),('vasavi',65),('teju',90)]
# print(sorted(l,key=lambda x:x[1],reverse=True))


# from functools import reduce
# l=[500,600,800,200,900,1000]
# print(reduce(lambda x,y:x+y,
#              list(filter(lambda x:x<=500,l)) +
#                     list(map(lambda x:x-(x*0.1),
#                              list(filter(lambda x:x>500,l))))))


# l=[{'name':'mohana','score':90},{'name':'asha','score':65},{'name':'yeshu','score':60}]
# print(sorted(list(map(lambda x:{**x,'grade' : 'pass' if x['score']>=60 else 'fail'},list(filter(lambda x:x['score']>=60,l)))),key=lambda x:x['score'],reverse=True))






