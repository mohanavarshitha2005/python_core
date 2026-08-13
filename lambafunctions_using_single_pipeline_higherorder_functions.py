# students = [
#     ("Ravi", 85),
#     ("Anil", 92),
#     ("Kiran", 85),
#     ("Bhanu", 92),
#     ("Deepa", 78)
# ]
# s1=sorted(students,key=lambda x:x[0],reverse=False)
# print(sorted(s1,key=lambda x:x[1],reverse=True))
# print(sorted(students,key=lambda x:x[1],reverse=True))
# print(sorted(students,key=lambda x:x[0],reverse=False))
# print(sorted(students,key=lambda x:(x[1],x[0]),reverse=(True,False)))
# print(sorted(s1,key=lambda x:x[0],reverse=False))
# s1=sorted(students,key=lambda x:x[0],reverse=True)
# print(sorted(s1,key=lambda x:x[1],reverse=False))


# l=['hii','bye','gdmrng','hello','se','oo']
# l1=print(sorted(l,key=lambda x:(len(x),x),reverse=False))
# # print(sorted(l1,key=lambda x:x,reverse=True))


# from functools import reduce
# l=[30,28,15,14,10,40]
# print(reduce(lambda x,y:x*y,list(map(lambda x:x+5,list(filter(lambda x:x%2==0 and x%5==0,l))))))


# from functools import reduce
# l=[3,7,6,4,30,20,19,67,68,70,12,24]
# l1=sorted(l,key=lambda x:x,reverse=False)
# print(reduce(lambda x,y:x*y,list(map(lambda x:x+3,list(filter(lambda x:x%2==0 and x%4!=0,l1))))))


from functools import reduce
l=['amma','nanna','amla','appa','billa','sms','bob']
l1=sorted(l,key=lambda x:(x[-1],len(x)),reverse=True)
l2=list(map(lambda x:x.lower(),list(filter(lambda x:x[-1]==x[0],l1))))
# l3=list(map(lambda x:x.lower(),list(filter(lambda x:x[-1]==x[0],l))))
# l3=l2+l3
print(reduce(lambda x,y:x + ' ' + y,l2))



# from functools import reduce
# transactions = [ {"type": "credit", "amount": 1000}, {"type": "debit", "amount": 500}, {"type": "credit", "amount": 2000} ]
# print(reduce(lambda x,y:x+y['amount'],list(filter(lambda x:x['type']=='debit',transactions)),reduce(lambda x,y:x+y['amount'],list(map(lambda x:{'type':x['type'],'amount':x['amount']+x['amount']*0.05},list(filter(lambda x:x['type']=='credit',sorted(transactions,key=lambda x:x['amount'],reverse=True))))),0)))

''
