
# Given two strings s and t of lengths m and n respectively, return the minimum window 
# substring
#  of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".
# The testcases will be generated such that the answer is unique.
# Example 1:
# Input: s = "ADOBECODEBANC", t = "ABC"
# Output: "BANC"
# Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        tcount={}
        scount={}
        for x in t:
            tcount[x] = 1+tcount.get(x,0)
        l=0
        have=0
        need=len(tcount)
        res=[-1,-1]
        resLen=float('infinity')
        for r in range(len(s)):
            x=s[r]
            scount[x]=1+scount.get(x,0)
            if x in tcount and scount[x]==tcount[x]:
                have +=1
            while(have==need):
                if (r-l+1)<resLen:
                    res=[l,r]
                    resLen=r-l+1
                scount[s[l]] -= 1
                if s[l] in tcount and scount[s[l]]<tcount[s[l]]:
                    have -=1
                l+=1
        l,r=res
        if resLen != float('infinity'):
            return s[l:r+1]
        else:
            return ""
