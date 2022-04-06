from collections import deque 

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        graph = [[] for i in range(numCourses)]
        indegree = [0] * (numCourses)
        for prerequisite in prerequisites :    
            x, y =prerequisite
            graph[y].append(x)
            indegree[x] += 1
        
        def judge ():
            final_list = []
            q = deque()
            
            for i in range(numCourses):
                if indegree[i] == 0:
                    q.append(i)
            
            while q:
                now = q.popleft()
                final_list.append(now)
                for i in graph[now]:
                    indegree[i] -= 1 
                    if indegree[i] == 0:
                        q.append(i)

            if len(final_list) == len(graph):
            
                return final_list

            else : 
            
                return []
                                       
        return (judge ())

        
    
            
        
        
        
            
            
            
            
        