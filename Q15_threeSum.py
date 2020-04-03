# 给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？
# 请你找出所有满足条件且不重复的三元组。

# 注意：答案中不可以包含重复的三元组。

#  

# 示例：

# 给定数组 nums = [-1, 0, 1, 2, -1, -4]，

# 满足要求的三元组集合为：
# [
#   [-1, 0, 1],
#   [-1, -1, 2]
# ]
# [-1, -1, 0, 0, 1, 1]

class Solution(object):
    def threeSum(self, nums):
        nums.sort()
        length = len(nums)
        result = []
        i = 0
        while i < length - 2:
            anser = nums[i]
            if anser > 0:
                return result
            j = i + 1
            k = length - 1
            
            while j < length - 1 and k > j:
                numj = nums[j]
                numk = nums[k]
                sumTemp = numj + numk
                if sumTemp == -anser:
                    result.append([anser, numj, numk])
                    j += 1
                    k -= 1
                    while j < length - 1 and nums[j] == numj:
                        j += 1
                    while k > j and nums[k] == numk:
                        k -= 1
                elif sumTemp > -anser:
                    k-=1
                    while k > j and nums[k] == numk:
                        k -= 1
                elif sumTemp < -anser:
                    j+=1
                    while j < length and nums[j] == numj:
                        j+=1
            i += 1
            while i < length and anser == nums[i]:
                i += 1
                
        return result

print(Solution().threeSum([-1, -1, 0, 0, 1, 1, 2]))