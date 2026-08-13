from functools import reduce
nums = [12, 10, 14, 76, 34, 35, 46, 25, 3, 100, 55]
# print(list(map(lambda x : x * 3,
               # list(filter(lambda x : x % 2 == 0, nums)))))
# print(list(map(lambda x : x ** 2,
#                list(filter(lambda x : x > 20, nums)))))
words = ['alice', 'jude', 'harry', 'olise', 'bob', 'benedict', 'catherine']
# print(list(map(lambda x : x.capitalize(),
#                list(filter(lambda x : len(x) > 4, words)))))

# print(list(map(lambda x : x + 10, list(filter(lambda x : x % 5 == 0, nums)))))
l = [1,2,3,4]
# print(reduce(lambda x , y: x - y, l))
# print(reduce(lambda x, y: x + y, l)/len(l))
