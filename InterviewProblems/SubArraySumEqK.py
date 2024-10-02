from collections import defaultdict
n=list(map(int,input().split()))
k=int(input())
if len(n)==0:
    print(0)
else:
    d=defaultdict(int)
    res=0
    curr_sum=0
    for i in n:
        curr_sum+=i
        if curr_sum==k:
            res+=1
        if (curr_sum-k) in d:
            res+=d[curr_sum-k]
        d[curr_sum]+=1
    print(res)