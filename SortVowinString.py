class Solution:
    def sortVowels(self, s: str) -> str:
        vow=[]
        result=''
        for i in s:
            if i in 'AEIOUaeiou':
                vow.append(i)
        vow.sort()
        j=0
        for i in s:
           if i in 'AEIOUaeiou':
               result+=vow[j]
               j+=1
           else:
               result+=i
        return result