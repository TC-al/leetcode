class Solution(object):
    def twoSum(self, nums, target):
        for x in range(len(nums)):
            for y in range(len(nums)):
                if nums[x] + nums[y] == target and x != y:
                    return [x, y]
        