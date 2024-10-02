import heapq
from collections import Counter
n=list(map(int,input().split()))
k=int(input())
c=Counter(n)
hm=[]
for i in c.keys():
    heapq.heappush(hm,(-c[i],i))
res=[]
for i in range(k):
    res.append(heapq.heappop(hm)[1])
print(res)