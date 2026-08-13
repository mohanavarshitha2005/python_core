# def apply_operation(a,b,op):
#     return op(a,b)
# op={'add':lambda x,y:x+y,
#     'subtract':lambda x,y:x-y,
#     'multiply':lambda x,y:x*y }
# print(apply_operation(30,20,op['add']))
# print(apply_operation(30,20,op['subtract']))
# print(apply_operation(30,20,op['multiply']))


# def make_greeting(name,prefix='hello',formatter=lambda x:x):
#     return prefix  +  name
# print(make_greeting('mohana',formatter=str.upper()))

# l=[2,3,4,6,7,8,5,12,76,4]
# print(list(map(lambda x:x**2,list(filter(lambda x:x%3==0,l)))))



# def apply_all(funcs,value):
#     result=[]
#     for i in funcs:
#        result.append(i(value))
#     return result
# funcs=[lambda x:2*x,
#      lambda x:3*x,
#      lambda x:4*x]
# value=int(input())
# print(apply_all(funcs,value))




# def apply_all(funcs,value):
#     result=[]
#     for i in funcs:
#        result.append(i(value))
#     return result
# op=[lambda x:2*x,
#      lambda x:3*x,
#      lambda x:4*x]
# print(apply_all(op,3))


# from functools import reduce
# result=[]
# def weighted_average(**scores):
#     for key,value in scores.items():
#         result.append(value)
#     print(result)
#     return result
# print(reduce(lambda x,y:x+y,weighted_average(maths=90,phy=70,eng=80,tel=99)))



# from functools import reduce
# def weighted_average(**scores):
#     result = []
#     for key,value in scores.items():
#         result.append(value)
#     print(result)
#     return reduce(lambda x,y:x+y,result)
# print(weighted_average(maths=90,phy=70,eng=80,tel=99))


# l=[{'mohana':50},{'asha':95},{'vasavi':80},{'teju':65}]
# result={}
# for d in l:
#       result.update(d)
# print(result)
# l2=list(map(lambda x:(x[0],x[1],'grade',':','pass' if x[1]>=60 else 'fail'),list(filter(lambda x:x[1]!=0,result.items()))))
# l1=sorted(l2,key=lambda x:x[1],reverse=True)
# print(l1)


# students=[{'name':'mohana','score':80},
#           {'name':'teju','score':85},
#           {'name':'vasavi','score':65}]
# l1=list(filter(lambda x:x['score']>=60,students))
# l2=list(map(lambda x:{**x,'grade':'pass'},l1))
# print(sorted(l2,key=lambda x:x['score'],reverse=True))


students=[{'name':'mohana','score':80},
          {'name':'teju','score':85},
          {'name':'vasavi','score':65}]
# l1=list(filter(lambda x:x['score']>=60,students))
# l2=list(map(lambda x:{**x,'grade':'pass'},list(filter(lambda x:x['score']>=60,students))))
print(sorted(list(map(lambda x:{**x,'grade':'pass'},list(filter(lambda x:x['score']>=60,students)))),key=lambda x:x['score'],reverse=True))




# l=[{'mohana':50,'asha':95,'vasavi':80,'teju':65}]
# result={}
# for d in l:
#       result.update(d)
# print(result)
# l2=list(map(lambda x:(x[0],x[1],'pass' if x[1]>=60 else 'fail'),list(filter(lambda x:x[1]>=60,result.items()))))
# l1=sorted(l2,key=lambda x:x[1],reverse=True)
# print(l1)



# l=[('mohana',60),('teja',75),('pooji',90)]
# d={'by_name':sorted(l,key=lambda x:x[0],reverse=False),
#    'by_score':sorted(l,key=lambda x:x[1],reverse=True),
#    'by_length':sorted(l,key=lambda x:len(x[0]),reverse=True)
#    }
# def sort(func,l):
#     return d[func]
# print(sort('by_name',l))
# print(sort('by_score',l))
# print(sort('by_length',l))


# from functools import reduce
# def calculator(*args,operation = "add",**options):
#     op={'add':lambda x,y:x+y,
#     'multiply':lambda x,y:x*y,
#     'max':lambda x,y:x if x>y else y,
#      'min':lambda x,y:y if x>y else x}
#     func =  op[operation]
#     res=args[0]
#     for i in args[1:]:
#         if options.get('show_steps'):
#             print(res,i,operation,func(res, i))
#         res=func(res,i)
#     return res
# print(calculator(20,30,40,80,100,operation='add',show_steps= True))
# print(calculator(20,30,40,80,100,operation='max',show_steps=True))
# print(calculator(20,30,40,80,100,operation='min',show_steps=False))
# print(calculator(20,30,40,80,100,operation='multiply',show_steps=True))