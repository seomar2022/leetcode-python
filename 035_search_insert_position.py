class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if nums[-1] < target:
            return len(nums)

        i = 0
        for num in nums:
            if num == target or num > target:
                return i
            else:
                i += 1
        return i

#https://leetcode.com/problems/search-insert-position?envType=problem-list-v2&envId=nz1q6a0h