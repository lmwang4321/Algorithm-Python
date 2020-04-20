class Solution:
    def longestValidParenthesis(self, s):
        maxlength = 0
        dp = [0]*len(s)
        for i in range(len(s)):
            if s[i] == ')':
                if s[i-1] == '(':
                    if i >= 2:
                        dp[i] = dp[i-2] + 2
                    else:
                        dp[i] = 2
                elif i-dp[i-1] > 0 and s[i-dp[i-1]-1] == '(':
                    if i - dp[i-1] >=2:
                        dp[i] = dp[i-1] + dp[i-dp[i-1]-2]+2
                    else:
                        dp[i] = dp[i-1] + 2
                maxlength = max(maxlength, dp[i])

        return maxlength