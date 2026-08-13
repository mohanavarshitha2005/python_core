from functools import reduce
transactions = [ {"type": "credit", "amount": 1000}, {"type": "debit", "amount": 500}, {"type": "credit", "amount": 2000} ]
print(reduce(lambda x,y:x+y['amount'],list(filter(lambda x:x['type']=='debit',transactions)),reduce(lambda x,y:x+y['amount'],list(map(lambda x:{'type':x['type'],'amount':x['amount']+x['amount']*0.05},list(filter(lambda x:x['type']=='credit',transactions)))),0)))
