class Merge:
    def mergesort(self,nums):
        if len(nums)<=1:
            return nums
        mid= len(nums)//2
        list1=self.mergesort(nums[mid:])
        list2=self.mergesort(nums[:mid])
        return self.merging(list1,list2)
    def merging(self,list1,list2):
        result=[]
        i=0
        j=0
        while(i<len(list1) and j<len(list2)):
            if list1[i]<=list2[j]:
                result.append(list1[i])
                i+=1
            else:
                result.append(list2[j])
                j+=1
        result += list1[i:]
        result += list2[j:]
        return result
lst=[1,2,3,4,3,2,7,6,5]
mergesortsolution = Merge()
print(mergesortsolution.mergesort(lst))


