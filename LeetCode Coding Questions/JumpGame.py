class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n=len(nums)
        maximumDist=0
        for i in range(n):
            if maximumDist<i:
                return False
            maximumDist=max(maximumDist,i+nums[i])
        return True
