class Solution:
    def reverseWords(self, s: str) -> str:
        lst= list(map(str,s.split()))
        lst=lst[::-1]
        res=""
        for i in range(len(lst)):
            if i<len(lst)-1:
                res+=lst[i]
                res+=" "
            if i==len(lst)-1:
                res+=lst[i]
        return res