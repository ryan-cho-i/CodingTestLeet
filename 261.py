from collections import deque

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        # First Condition
        
        if n == len(edges) - 1 :
            return false 
        
        # Second Condition 
        
        # graph
        
        graph = [[] for _ in range (n)]
        for a, b in edges :
            graph[a].append(b)
            graph[b].append(a)
        
        parent = {0:-1}
        q = deque([0])
        
        while q :
            node = q.popleft()
            for neighbor in graph[node]:
                if neighbor == parent[node]:
                    continue
                if neighbor in parent:
                    return False
                parent[neighbor] = node
                q.append(neighbor)
                
        return len(parent) == n
            
            
        