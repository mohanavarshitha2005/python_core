# n=int(input())
# n1=int(input())
# for i in range(1,n+1):
#     for j in range(1,n1+1):
#         if i>=j:
#             print("*",end=" ")
#     print()



# n=int(input())
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if i==j:
#             print(i,end=" ")
#         elif i<j:
#             print(j,end=" ")
#     print()


# n=int(input())
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if i==j:
#             print(i,end=" ")
#         elif i>j:
#             print(j,end=" ")
#     print()

n=int(input())
for i in range(n,0,-1):
    for j in range(n,0,-1):
        if i+j==n+1:
            print(i,end=" ")
        elif i+j>n+1:
            print(j,end=" ")
    print()

