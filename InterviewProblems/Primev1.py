n=int(input())
prm=[True]*(n+1)
prm[0]=prm[1]=False
i=1
while i*i<=n+1:
    if prm[i]:
        for j in range(i*i,n+1,i):
            prm[j]=False
    i+=1
res=[]
for i,j in enumerate(prm):
    if j:
        res.append(i)
print(res)
