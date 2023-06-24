class Solution:
    def firstUniqChar(self, s: str) -> int:
        import collections
        counter = collections.Counter(s)
        print(counter)
        for i in range(len(s)):
            if counter[s[i]]==1:
                return i
        return -1
solution=Solution()
print(solution.firstUniqChar("vamsiamsv"))