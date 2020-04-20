class solution:
    def removeDuplicate(self, nums):
        i = 0
        for j in range(1,len(nums)):
            if nums[i] != nums[j]:
                i += 1
                nums[i] = nums[j]

        return nums[:i+1]

s = solution()
nums = [1,2,4,4,7,8,10,10,12]
res = s.removeDuplicate(nums)
print(res)