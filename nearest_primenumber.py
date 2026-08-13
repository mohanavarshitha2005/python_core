def isprime(n):
    fc=0
    for i in range(1,n+1):
        if n%i==0:
            fc+=1
    if fc==2:
        return True
    return False
n=int(input())
i=n+1
j=n-1
while True:
    if isprime(i):
        np=i
        break
    i+=1
while True:
    if isprime(j):
        pp=j
        break
    j-=1
npd=np-n
ppd=n-pp
if npd<ppd:
    print(np)
elif ppd<npd:
    print(pp)
else:
    print(pp,np)