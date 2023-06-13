class Solution:
    def search(self, nums: list[int], target: int) -> int:
        i=0
        j = len(nums)-1
        while i<=j:
            mid = (i+j)//2
            if nums[mid]==target:
                return mid
            elif nums[mid]>target:
                j = mid-1
            else:
                i = mid+1
        return -1
target=5
nums= [1,2,3,54,5,6,7]
solution = Solution()
print(solution.search(nums, target))