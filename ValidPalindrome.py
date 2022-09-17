class Solution:
    def isPalindrome(self, s: str) -> bool:
        res=''
        for i in s.lower():
            if i.isalnum():
                res+=i
        print(res)
        return res==res[::-1]

s=Solution()
assert True==s.isPalindrome("A man, a plan, a canal: Panama")
assert False==s.isPalindrome("race a car")