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


l=[{'name':'mohana','score':60},
   {'name':'asha','score':90},
   {'name':'vasavi','score':85}]
print(sorted(list(map(lambda x:{**x,'grade' : "pass" if x['score']>=60 else "fail"},list(filter(lambda x:x['score']>=60,l)))),key=lambda x:x['score'],reverse=True))


