from typing import List
import functools
class Solution:
    def largestNumber(self, nums: List[int]) -> str:

        def custom_sort(a,b):
            if a+b<b+a:
                return -1
            elif a+b>b+a:
                return 1
            else:
                return 0

        strnums=list(map(str,nums))
        strnums.sort(key=functools.cmp_to_key(custom_sort),reverse=True)
        return str(int(''.join(strnums)))