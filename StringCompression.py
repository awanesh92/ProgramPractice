from typing import List
class Solution:
    def compress(self, chars: List[str]) -> int:
        if len(chars) < 2: return len(chars)
        result, last_char, cnt = [chars[0]], chars[0], 1

        for i in chars[1:]:
            if last_char == i:
                cnt += 1
            else:
                if cnt > 1:
                    result.append(str(cnt))
                result.append(i)
                cnt = 1
            last_char = i
        if cnt > 1:
            result.append(str(cnt))
        op = ''.join(result)
        for i in range(len(op)):
            chars[i] = op[i]
        print(chars[:len(op)])
        return len(op)

        # #Approach 2
        # i, ans = 0, 0
        # while i < len(chars):
        #     temp = chars[i]
        #     cnt = 0
        #     while i < len(chars) and chars[i] == temp:
        #         cnt += 1
        #         i += 1
        #     chars[ans] = temp
        #     ans += 1
        #     if cnt > 1:
        #         for c in str(cnt):
        #             chars[ans] = c
        #             ans += 1
        # return ans

s=Solution()
assert 6 == s.compress(["a","a","b","b","c","c","c"])