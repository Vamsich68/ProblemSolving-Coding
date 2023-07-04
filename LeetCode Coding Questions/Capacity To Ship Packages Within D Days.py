class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def findDays(weights, capacity):
            res=1
            load=0
            for i in range(len(weights)):
                if load+weights[i]>capacity:
                    res+=1
                    load=weights[i]
                else:
                    load+=weights[i]
            return res
        low=max(weights)
        high=sum(weights)
        while(low<=high):
            mid=(low+high)//2
            NumberOfDays=findDays(weights,mid)
            if NumberOfDays<=days:
                high=mid-1
            else:
                low=mid+1
        return low