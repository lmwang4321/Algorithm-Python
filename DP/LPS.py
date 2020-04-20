class Solution:
    def longestPalindrome(self, s):
        P = [[0]*len(s) for _ in range(len(s))]
        for i in range(len(s)):
            P[i][i] = 1
            if i <= len(s) - 2 and s[i] == s[i+1]:
                P[i][i+1] = 1
        a = 1



s = Solution()
res = s.longestPalindrome('geeksforgeeks')