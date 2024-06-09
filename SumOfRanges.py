from typing import List
class Solution:

    def subArrayRanges(self, nums: List[int]) -> int:
        return self.sumSubarrayMax(nums) - self.sumSubarrayMins(nums)

    def sumSubarrayMax(self, arr: List[int]) -> int:
        n = len(arr)
        leftArr = [0] * n
        rightArr = [0] * n
        stk = []  # decreasing monotonic stack
        result = 0
        # for left side calculation
        for i in range(n):
            cnt = 1
            while stk and stk[-1][0] < arr[i]:
                cnt += stk[-1][1]
                stk.pop()
            stk.append((arr[i], cnt))
            leftArr[i] = cnt
        stk.clear()
        for i in range(n - 1, -1, -1):
            cnt = 1
            while stk and stk[-1][0] <= arr[i]:
                cnt += stk[-1][1]
                stk.pop()
            stk.append((arr[i], cnt))
            rightArr[i] = cnt

        for i in range(n):
            result = (result + (arr[i] * (leftArr[i] * rightArr[i])))
        return result

    def sumSubarrayMins(self, arr: List[int]) -> int:
        n = len(arr)
        leftArr = [0] * n
        rightArr = [0] * n
        stk = []  # increasing monotonic stack
        result = 0
        # for left side calculation
        for i in range(n):
            cnt = 1
            while stk and stk[-1][0] > arr[i]:
                cnt += stk[-1][1]
                stk.pop()
            stk.append((arr[i], cnt))
            leftArr[i] = cnt
        stk.clear()
        for i in range(n - 1, -1, -1):
            cnt = 1
            while stk and stk[-1][0] >= arr[i]:
                cnt += stk[-1][1]
                stk.pop()
            stk.append((arr[i], cnt))
            rightArr[i] = cnt

        for i in range(n):
            result = (result + (arr[i] * (leftArr[i] * rightArr[i])))
        return result