"""
this is the python program
for the minimum-delay routing problem in
DP.pdf
"""

class Solution:
    def minDelay(self, arr):
        dp = [[0]*len(arr) for _ in range(len(arr[0]))]
        for i in range(len(arr[0])):
            dp[0][i] = arr[-1][i]
        for i in range(1, len(arr)):
            for j in range(len(arr[0])):
                if i % 2 == 1 and j != len(arr[0]) - 1:
                    dp[i][j] = min(dp[i-1][j]+arr[-i-1][j], dp[i-1][j+1]+arr[-i-1][j])
                if i % 2 == 1 and j == len(arr[0]) - 1:
                    dp[i][j] = dp[i-1][j] + arr[-i-1][j]
                if i % 2 == 0 and j != 0:
                    dp[i][j] = min(dp[i-1][j]+arr[-i-1][j], dp[i-1][j-1]+arr[-i-1][j])
                if i % 2 == 0 and j == 0:
                    dp[i][j] = dp[i-1][j] + arr[-i-1][j]
            return min(dp[-1])


arr = [[2, 5, 7, 4, 5, 6],
       [3, 6, 7, 3, 9, 4],
       [6, 5, 2, 6, 3, 9],
       [3, 9, 6, 3, 3, 2],
       [3, 5, 7, 9, 1, 3],
       [8, 2, 6, 5, 5, 3]]

s =  Solution()
mindelay = s.minDelay(arr)
print(mindelay)