class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        def visitIslands(grid,i,j,rows,cols):
            if (i<0 or i>=rows or j<0 or j>=cols or grid[i][j]!="1"):
                return
            grid[i][j]="2"
            visitIslands(grid,i-1,j,rows,cols)
            visitIslands(grid,i+1,j,rows,cols)
            visitIslands(grid,i,j-1,rows,cols)
            visitIslands(grid,i,j+1,rows,cols)
        rows=len(grid)
        cols = len(grid[0])
        result=0
    

        if rows==0:
            return 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]=="1":
                    visitIslands(grid,i,j,rows,cols)
                    result+=1
        return result