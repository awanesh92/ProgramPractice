from typing import List
from collections import defaultdict
class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        top=["Gold Medal", "Silver Medal", "Bronze Medal"]
        sorted_score=sorted(score,reverse=True)
        rank_mapping={score:top[i] if i<3 else str(i+1) for i,score in enumerate(sorted_score)}
        return [rank_mapping[score] for score in score]
