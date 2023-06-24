class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        column=set()
        positive=set()
        negative=set()
        mat=[["."]*n for i in range(n) ]
        res=[]
        def backtracking(r):
            if r==n:
                temp=["".join(row) for row in mat]
                res.append(temp)
                return
            for j in range(n):
                if j in column or (r+j) in positive or (r-j) in negative:
                    continue
                column.add(j)
                positive.add(r+j)
                negative.add(r-j)
                mat[r][j]="Q"
                backtracking(r+1)
                column.remove(j)
                positive.remove(r+j)
                negative.remove(r-j)
                mat[r][j]="."
        backtracking(0)
        return res