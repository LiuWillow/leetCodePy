learl# 给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那
#  两个 整数，并返回他们的数组下标。

# 你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。

# 示例:

# 给定 nums = [2, 7, 11, 15], target = 9

# 因为 nums[0] + nums[1] = 2 + 7 = 9
# 所以返回 [0, 1]

class Solution(object):
    # 暴力版本
    def twoSumForce(self, nums, target):
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if (nums[i] + nums[j] == target):
                    return [i, j]

    # 字典版本
    def twoSumDict(self, nums, target):
        dic = {}
        for i in range(len(nums)):
            key = target - nums[i]
            if(key in dic):
                return [dic[key], i]
            else:
                dic[nums[i]] = i

    print(twoSumDict(1, [2, 7, 11, 15], 17))