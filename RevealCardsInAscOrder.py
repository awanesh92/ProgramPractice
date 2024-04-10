from collections import deque
from typing import List
class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort()
        n=len(deck)
        result=[0]*n

        indx=deque(range(n))

        for card in deck:
            idx=indx.popleft()
            result[idx]=card
            if indx:
                indx.append(indx.popleft())
        return result