class Solution:
    def getTotalIsles(self, grid: list[list[str]]) -> int:
        if not grid:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        visited = [[False] * cols for _ in range(rows)]

        def dfs(r, c):
           
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == 'W' or visited[r][c]:
                return
            
           
            visited[r][c] = True
            
           
            dfs(r + 1, c) 
            dfs(r - 1, c)  
            dfs(r, c + 1)  
            dfs(r, c - 1) 

        island_count = 0
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 'L' and not visited[i][j]:
                    
                    dfs(i, j)
                    island_count += 1
        
        return island_count


if __name__ == "__main__":
    solution = Solution()
    
   
    result1 = solution.getTotalIsles([
        ["L", "L", "L", "L", "W"],
        ["L", "L", "W", "L", "W"],
        ["L", "L", "W", "W", "W"],
        ["W", "W", "W", "W", "W"]
    ])
    print(result1) 

   
    result2 = solution.getTotalIsles([
        ["L", "L", "W", "W", "W"],
        ["L", "L", "W", "W", "W"],
        ["W", "W", "L", "W", "W"],
        ["W", "W", "W", "L", "L"]
    ])
    print(result2)  

    
    result3 = solution.getTotalIsles([
        ["W", "W", "W"],
        ["W", "W", "W"],
        ["W", "W", "W"]
    ])
    print(result3)  

    
    result4 = solution.getTotalIsles([
        ["L", "W", "L"],
        ["W", "L", "W"],
        ["L", "W", "L"]
    ])
    print(result4)  
