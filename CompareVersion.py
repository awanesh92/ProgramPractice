class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1=list(map(int,version1.split(".")))
        v2=list(map(int,version2.split(".")))

        n,m=len(v1),len(v2)
        if n<m:
            v1+=[0]*(m-n)
        elif n>m:
            v2+=[0]*(n-m)
        for i in range(max(n,m)):
            if v1[i]<v2[i]:
                return -1
            elif v1[i]>v2[i]:
                return 1
        return 0