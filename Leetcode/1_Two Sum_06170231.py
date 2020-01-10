class Solution(object):
    def twoSum(self, nums, target):
        s = {}
        for i, num in enumerate(nums):
            n = target - num
            if n not in s:
                s[num] = i
            else:
                return [s[n], i]
