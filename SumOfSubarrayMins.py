from typing import List
class Solution:
    mod = 10 ** 9 + 7
    def sumSubarrayMins(self, arr: List[int]) -> int:
        n=len(arr)
        leftArr=[0]*n
        rightArr=[0]*n
        stk=[]
        result=0
        #for left side calculation
        for i in range(n):
            cnt=1
            while stk and stk[-1][0]>arr[i]:
                cnt+=stk[-1][1]
                stk.pop()
            stk.append((arr[i],cnt))
            leftArr[i]=cnt
        stk.clear()
        for i in range(n-1,-1,-1):
            cnt=1
            while stk and stk[-1][0]>=arr[i]:
                cnt+=stk[-1][1]
                stk.pop()
            stk.append((arr[i],cnt))
            rightArr[i]=cnt

        for i in range(n):
            result=(result+(arr[i]*(leftArr[i]*rightArr[i]))%self.mod)%self.mod

        return result