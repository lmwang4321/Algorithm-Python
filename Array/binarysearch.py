class BinarySearch:
    def traditional(self, nums, target):
        n = len(nums)
        mid = nums[n//2]
        res = 0
        if n == 1 and nums[0] != target:
            return -1
        if nums[n//2] > target:
            res = self.traditional(nums[:n//2], target)
        elif nums[n // 2] < target:
            res = self.traditional(nums[n//2:], target)
        elif nums[n // 2] == target:
            return n // 2
        return res

    def search_in_rotated(self, nums, target):


bs = BinarySearch()
nums = [0, 1, 2, 4, 5, 6, 7]
res = bs.traditional(nums, 3)
print(res)