class Solution:

    def permute(self, nums):
        if len(nums) == 0:
            return []

        used = [False] * len(nums)
        res = []
        self.__dfs(nums, 0, [], used, res)
        return res

    def __dfs(self, nums, index, pre, used, res):
        # 先写递归终止条件
        if index == len(nums):
            res.append(pre.copy())
            return

        for i in range(len(nums)):
            if not used[i]:
                # 如果没有用过，就用它
                used[i] = True
                pre.append(nums[i])

                # 在 dfs 前后，代码是对称的
                self.__dfs(nums, index + 1, pre, used, res)

                used[i] = False
                pre.pop()

s = Solution()
res = s.permute([1,2,3])
print(res)