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

s=Solution()
assert 6 == s.compress(["a","a","b","b","c","c","c"])