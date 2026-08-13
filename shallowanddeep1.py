import copy
ticket=[['a1','standard',250],['a2','premium',550],['a3','recliner',750]]
print(ticket)
shallow_ticket=copy.copy(ticket)
shallow_ticket[0][1]='premium'
print(ticket)
print(shallow_ticket)
deep_ticket=copy.deepcopy(ticket)
deep_ticket[2][1]='acroom'
print(ticket)
print(deep_ticket)

