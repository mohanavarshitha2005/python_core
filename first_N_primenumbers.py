def isprime(n):
    fc=0
    for i in range(1,n+1):
        if n%i==0:
            fc+=1
    if fc==2:
        return True
    return False
n=int(input())
i=1
c=0
while True:
    if isprime(i):
        print(i,end=" ")
        c+=1
        if c==n:
            break
    i+=1