from collections import deque
from typing import List
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj=[[] for _ in range(numCourses)]

        for i in range(len(prerequisites)):
            adj[prerequisites[i][1]].append(prerequisites[i][0])

        indegree=[0]*numCourses

        for i in range(numCourses):
            for j in adj[i]:
                indegree[j]+=1

        q=deque()
        for i in range(numCourses):
            if indegree[i]==0:
                q.append(i)
        topo=[]
        while q:
            node=q.popleft()
            topo.append(node)

            for neigh in adj[node]:
                indegree[neigh]-=1
                if indegree[neigh]==0:
                    q.append(neigh)
        if len(topo)==numCourses:
            return True
        else:
            return False