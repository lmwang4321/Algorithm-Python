"""
给定一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？找出所有满足条件且不重复的三元组。

注意：答案中不可以包含重复的三元组。

例如, 给定数组 nums = [-1, 0, 1, 2, -1, -4]，

满足要求的三元组集合为：
[
  [-1, 0, 1],
  [-1, -1, 2]
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/3sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        res = []
        k = 0
        for k in range(len(nums) - 2):
        	"""
        	当 nums[k] > 0 时直接break跳出：因为 nums[j] >= nums[i] >= nums[k] > 0，
        	即 33 个数字都大于 00 ，在此固定指针 k 之后不可能再找到结果了

			作者：jyd
			链接：https://leetcode-cn.com/problems/two-sum/solution/3sumpai-xu-shuang-zhi-zhen-yi-dong-by-jyd/
			来源：力扣（LeetCode）
			著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
        	"""
        	if nums[k] > 0: break

        	"""
        	当 k > 0且nums[k] == nums[k - 1]时即跳过此元素nums[k]：
        	因为已经将 nums[k - 1] 的所有组合加入到结果中，本次双指针搜索只会得到重复组合。

			作者：jyd
			链接：https://leetcode-cn.com/problems/two-sum/solution/3sumpai-xu-shuang-zhi-zhen-yi-dong-by-jyd/
			来源：力扣（LeetCode）
			著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
        	"""
        	if k > 0 and nums[k] == nums[k-1]: continue
        	"""
        	i，j 分设在数组索引 (k, len(nums))(k,len(nums)) 两端，
        	当i < j时循环计算s = nums[k] + nums[i] + nums[j]，并按照以下规则执行双指针移动：
			当s < 0时，i += 1并跳过所有重复的nums[i]；
			当s > 0时，j -= 1并跳过所有重复的nums[j]；
			当s == 0时，记录组合[k, i, j]至res，执行i += 1和j -= 1并跳过所有重复的nums[i]和nums[j]，防止记录到重复组合。

			作者：jyd
			链接：https://leetcode-cn.com/problems/two-sum/solution/3sumpai-xu-shuang-zhi-zhen-yi-dong-by-jyd/
			来源：力扣（LeetCode）
			著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
			"""
        	i = k + 1
        	j = len(nums) - 1
        	while i < j:
        		s = nums[k] + nums[i] + nums[j]
        		if s < 0:
        			i += 1
        			while i < j and nums[i] == nums[i-1]: i += 1
        		elif s > 0:
        			j -= 1
        			while i < j and nums[j] == nums[j+1]: j -= 1
        		else:
        			res.append(nums[k], nums[i], nums[j])
        			i += 1
        			j -= 1
        			while i < j and nums[i] == nums[i-1]: i += 1 
        			while i < j and nums[j] == nums[j+1]: j -= 1

        return res



nums = [-1, 0, 1, 2, -1, -4]
