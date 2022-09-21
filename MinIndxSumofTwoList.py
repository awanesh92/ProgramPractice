from typing import List
class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        dict1={}
        for i,e in enumerate(list1):
            dict1[e]=i
        dict2={}
        m=len(list1)+len(list2)-1
        for i,e in enumerate(list2):
            if e in dict1:
                dict2[e]=dict1[e]+1
                m=min(m,dict2[e])
        res=[]
        for i in dict2:
            if dict2[i]==m:
                res.append(i)
        return res

s=Solution()
assert ["Shogun"]==s.findRestaurant(["Shogun","Tapioca Express","Burger King","KFC"],
                                    ["Piatti","The Grill at Torrey Pines","Hungry Hunter Steakhouse","Shogun"])