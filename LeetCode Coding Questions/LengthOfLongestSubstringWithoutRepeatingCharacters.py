class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        st = ''
        res = 0
        for i in s:
            if i not in st:
                st += i
                res = max(res, len(st))
                print(st)
            else:
                index = st.index(i)
                st = st[index + 1:] + i
                print(st)
        return res
solution=Solution()
print(solution.lengthOfLongestSubstring("abcdbcdb"))