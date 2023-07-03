class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        dp=[1]*len(nums)
        for i in range(len(nums)-1,-1,-1):
            for j in range(i+1,len(nums)):
                if nums[i]<nums[j]:
                    dp[i]=max(dp[i],1+dp[j])
        return max(dp)
solution= Solution()
print(solution.lengthOfLIS([1,2,3,2,1,4,5,4,6]))