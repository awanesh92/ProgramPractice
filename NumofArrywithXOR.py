from collections import defaultdict
class Solution:
    def solve(self, a, k):
        xr=0
        cnt = 0
        mp=defaultdict(int)
        mp[xr]=1
        for i in range(len(a)):
            xr=xr^a[i]
            x=xr^k
            cnt+=mp[x]
            mp[xr]+=1
        return cnt