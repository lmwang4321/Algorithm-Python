class Solution:
    def LIS(self, nums):
        dp = [1]*len(nums)
        for i in range(len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[j]) + 1
        return max(dp)