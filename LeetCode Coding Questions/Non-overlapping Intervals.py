class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        result=0
        previous = intervals[0][1]
        for i, j in intervals[1:]:
            if i>=previous:
                previous=j
            else:
                result+=1
                previous =  min(j, previous)
        return result
