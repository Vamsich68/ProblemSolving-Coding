class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def partition(lst,i,j):
            while(i<j):
                lst[i],lst[j]=lst[j],lst[i]
                i+=1
                j-=1

            return lst
        k=k%len(nums)
        nums= partition(nums,0,len(nums)-1)
        nums= partition(nums,0,k-1)
        nums= partition(nums,k,len(nums)-1)