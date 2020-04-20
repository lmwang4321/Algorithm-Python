def partition(nums, left, right):
    pivot = nums[left]
    j = left
    for i in range(left+1, right):
        if nums[i] < pivot:
            nums[j], nums[i] = nums[i], nums[j]
            j += 1
    return j

nums = [6,5,3,1,2,9,12,10]
res = partition(nums,0,len(nums))
print(res)