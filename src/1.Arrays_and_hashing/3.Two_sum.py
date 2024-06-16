# https://leetcode.com/problems/two-sum/

def twoSum(self, nums, target):
    dict = {}
    for i in range(len(nums)):
        num = nums[i]
        diff = target - num
        hasDiff = diff in dict
        if hasDiff:
            return [dict[diff], i]
        if num not in dict:
            dict[num] = i
    return [0,1]