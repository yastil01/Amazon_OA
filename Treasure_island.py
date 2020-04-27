class Solution:
    def tresureIslands(self, grid: List[List[str]]) -> int:
        if len(grid)==0 or len(grid[0])==0: return -1
        
        seen = {}
        self.min_steps = float('inf')
        
        def dfs(row,col,curr_steps):
            if row<0 or row>=len(grid) or col<0 or col>=len(grid[0])\
                or grid[row][col]=='D' or (row,col) in seen:
                return

            if grid[row][col] == 'X':
                self.min_steps = min(curr_steps, self.min_steps)
                return
            
            seen[(row,col)] = 1
            
            dfs(row,col+1,curr_steps+1)
            dfs(row+1,col,curr_steps+1)
            dfs(row,col-1,curr_steps+1)
            dfs(row-1,col,curr_steps+1)
            
            del seen[(row,col)]
            
        dfs(0,0,0)
        if self.min_steps==float('inf'): return -1
        return self.min_steps
    
obj = Solution()
grid = [['O', 'O', 'O', 'O'], ['D', 'O', 'D', 'O'], ['O', 'O', 'O', 'O'], ['X', 'D', 'D', 'O']]
grid1 = [['X', 'O', 'O', 'O'], ['D', 'O', 'D', 'O'], ['O', 'O', 'O', 'O'], ['D', 'D', 'D', 'O']]
grid2 = [[]]
grid3 = [['O', 'O', 'O', 'O'], ['D', 'O', 'D', 'O'], ['O', 'O', 'O', 'O'], ['D', 'D', 'D', 'O']]
grid4 = [['O', 'O', 'O', 'X'], ['D', 'O', 'D', 'O'], ['O', 'O', 'O', 'O'], ['D', 'D', 'D', 'O']]
grid5 = [['O', 'O'], ['O', 'O'], ['X', 'O']]

print(obj.tresureIslands(grid))
print(obj.tresureIslands(grid1))
print(obj.tresureIslands(grid2))
print(obj.tresureIslands(grid3))
print(obj.tresureIslands(grid4))
print(obj.tresureIslands(grid5))
