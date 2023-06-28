class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        index=-1
        n=len(nums)
        for i in range(n-2,-1,-1):
            if nums[i]<nums[i+1]:
                index=i
                break
        if index==-1:
            res=nums[::-1]
            nums.reverse()
            return
            #print(res)
        for j in range(n-1,-1,-1):
            if nums[j]>nums[index]:
                nums[j],nums[index]=nums[index],nums[j]
                break
        temp=nums[index+1:]
        nums[index+1:]=temp[::-1]
        return nums

