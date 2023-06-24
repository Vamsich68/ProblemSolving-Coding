class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        '''
        n=len(nums)
        sum = (n*(n+1))/2
        for i in nums:
            sum -=i
        return int(sum)
        '''
        res=0
        for i in nums:
            res=res^i
        for j in range(1,len(nums)+1):
            res=res^j
        return res