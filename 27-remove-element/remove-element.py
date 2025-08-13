class Solution(object):
    def removeElement(self, nums, val):
        count = 0
        for x in nums:
            if val != x:
                nums[count] = x
                count+=1
        return count