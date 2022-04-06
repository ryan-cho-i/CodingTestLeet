class Solution:
    
    def numIslands(self, grid: List[List[str]]) -> int:
        
        def bfs (grid, x, y):
        
            dx, dy = [-1,1,0,0],[0,0,-1,1]
            
            grid[x][y] = '0'

            for i in range(4):

                nx = x + dx[i]
                ny = y + dy[i]

                if 0<=nx<len(grid) and 0<=ny<len(grid[0]) and grid[nx][ny] == '1':

                    bfs (grid, nx, ny)
                    
        cnt = 0 
               
        for i in range(len(grid)) :
            
            for j in range(len(grid[0])):
        
                if grid[i][j] == '0' :
                
                    continue 

                else : 

                    bfs (grid, i, j)
                    cnt += 1
                    
        return cnt