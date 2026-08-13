s=int(input())
e=int(input())
c=0
for i in range(s,e+1):
    if i%2==0:
        c+=1
        if c%2!=0:
            print(i,end=" ")
        if c>1:
            print(",",end=" ")
