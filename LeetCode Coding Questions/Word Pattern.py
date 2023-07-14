# Given a pattern and a string s, find if s follows the same pattern.
# Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s.
# Example 1:
# Input: pattern = "abba", s = "dog cat cat dog"
# Output: true

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        dic = {}
        temp = s.split()
        if len(pattern) != len(temp):
            return False
        if len(set(pattern)) != len(set(temp)):
            return False
        for i in range(len(pattern)):
            if pattern[i] not in dic:
                dic[pattern[i]] = temp[i]
            elif dic[pattern[i]] != temp[i]:
                return False
        return True
