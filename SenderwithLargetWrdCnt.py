from typing import List
from collections import defaultdict
class Solution:
    def largestWordCount(self, messages: List[str], senders: List[str]) -> str:
        #Approach 1
        # dict_ = defaultdict(int)
        # max_ = (0, '')
        # for m,s in zip(messages, senders):
        #     dict_[s] += m.count(' ')+1
        #     max_ = max(max_, (dict_[s], s))
        # print(max_)
        # return max_[1]
        #Approach 2
        j=0
        hp={}
        for s in senders:
            if s in hp:
                hp[s]+=len(messages[j].split())
                j+=1
            else:
                hp[s]=len(messages[j].split())
                j+=1
        listx=list()
        for k in hp:
            listx.append([hp[k],k])
        listx.sort()
        return listx[-1][1]

s=Solution()
assert "Alice"==s.largestWordCount(["Hello userTwooo","Hi userThree","Wonderful day Alice","Nice day userThree"],
                                   ["Alice","userTwo","userThree","Alice"])