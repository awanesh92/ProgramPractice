class Solution:
    def findTwoElement( self,arr, n):
        xr=0
        for i in range(n):
            xr^=arr[i]
            xr^=(i+1)
        bitNo=0
        #find the lestMost bit of the final XOR number
        while True:
            if xr & (1<<bitNo)!=0:
                break
            else:
                bitNo+=1
        #now separate 1 and 0 accordingly
        one,zero=0,0
        for i in range(n):
            if (arr[i] & (1<<bitNo))!=0:
                one^=arr[i]
            else:
                zero^=arr[i]
        for i in range(1,n+1):
            if (i & (1 << bitNo)) != 0:
                one ^= i
            else:
                zero ^= i
        if one in arr:
            return [one,zero]
        else:
            return [zero,one]