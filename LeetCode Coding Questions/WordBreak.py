
# Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.

# Note that the same word in the dictionary may be reused multiple times in the segmentation.

# Example 1:

# Input: s = "leetcode", wordDict = ["leet","code"]
# Output: true
# Explanation: Return true because "leetcode" can be segmented as "leet code".
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        '''
        for i in wordDict:
            if i not in s or len(s)==0:
                return False
            if i in s:
                s=s.replace(i,'')
                #print(s)
        return True
        '''
        dp=[False]*(len(s)+1)
        dp[len(s)]=True
        for i in range(len(s)-1,-1,-1):
            for j in wordDict:
                if i + len(j)<=len(s) and s[i:i+len(j)]==j:
                    dp[i]=dp[i+len(j)]
                if dp[i]:
                    break
        return dp[0]
