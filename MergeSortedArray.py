from typing import List
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1[m:]=nums2
        nums1.sort()

s=Solution()
nums1,nums2=[1,2,3,0,0,0],[2,5,6]
s.merge(nums1,3,nums2,3)
assert [1,2,2,3,5,6]==nums1

