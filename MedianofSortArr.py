from typing import List
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        total = len(nums1) + len(nums2)
        half = total // 2
        # A is smaller of the two array
        if len(B) < len(A):
            A, B = B, A

        l, r = 0, len(A) - 1
        while True:
            # get midindx of the array A
            i = (l + r) // 2
            # get left array end of B as it will be half-the index of leftmost element in A
            j = half - i - 2

            # to get leftmost element of left side and righmost of right side of merged array for mid
            Aleft = A[i] if i >= 0 else float("-infinity")
            Aright = A[i + 1] if (i + 1) < len(A) else float("infinity")
            Bleft = B[j] if j >= 0 else float("-infinity")
            Bright = B[j + 1] if (j + 1) < len(B) else float("infinity")
            if Aleft <= Bright and Bleft <= Aright:
                if total % 2:
                    return min(Aright, Bright)
                else:
                    return (max(Aleft, Bleft) + min(Bright, Aright)) / 2
            # when B is having the element in the left side of merged array
            elif Aleft > Bright:
                r = i - 1  # reducing the right pointer from smaller array
            else:
                l = i + 1

s=Solution()
assert 2.50000==s.findMedianSortedArrays([1,2],[3,4])
assert 2.00000==s.findMedianSortedArrays([1,2],[3])