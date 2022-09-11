from typing import List
import re, collections
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        paragraph, banned = re.findall(r"[^!?',;\.\s]+", paragraph.lower()), set(banned)
        cnt = collections.Counter(word for word in paragraph if word not in banned)
        return max(cnt, key=cnt.get)

s=Solution()
assert "ball"==s.mostCommonWord("Bob hit a ball, the hit BALL flew far after it was hit.",["hit"])