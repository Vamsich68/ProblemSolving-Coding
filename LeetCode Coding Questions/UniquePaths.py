class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        res=[1 for i in range(n)]
        for j in range(m-1):
            temp=[1]*n
            for k in range(n-2,-1,-1):
                temp[k]=temp[k+1]+res[k]
            res=temp
        return res[0]