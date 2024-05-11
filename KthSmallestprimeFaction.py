from typing import List
class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        left,right=0,1
        n=len(arr)
        res=[]
        while left<=right:
            mid=left+(right-left)/2
            total,j,num,den,maxfrac=0,1,0,0,0
            for i in range(n):
                while j<n and arr[i]>=arr[j]*mid:
                    j+=1
                total+=n-j
                if j<n and maxfrac<arr[i]*1.0/arr[j]:
                    maxfrac=arr[i]*1.0/arr[j]
                    num=i
                    den=j

            if total==k:
                res=[arr[num],arr[den]]
                break
            if total>k:
                right=mid
            else:
                left=mid
        return res