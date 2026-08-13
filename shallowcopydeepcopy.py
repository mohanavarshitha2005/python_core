list=[['hii','hello'],['wra','wya'],['seeyou','bye']]
print(list)
import copy
shallow_cpy=copy.copy(list)
shallow_cpy[0][0]='hieeee'
print(list)
print(shallow_cpy)
print(id(list))
print(id(shallow_cpy))
print(id(shallow_cpy[0]))
print(id(list[0]))
deep_cpy=copy.deepcopy(list)
deep_cpy[1][1]='tea'
print(list)
print(deep_cpy)
print(id(list))
print(id(deep_cpy))
print(id(deep_cpy[1]))
print(id(list[1]))







