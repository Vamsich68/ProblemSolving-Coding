class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s)==0:
            return True
        i,j=0,0
        while(i<len(s) and j<len(t)):
            if i==len(s)-1 and s[i]==t[j]:
                return True
            if i<len(s) and s[i]==t[j]:
                i+=1
                j+=1
            else:
                j+=1
        return False