class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        nums_len = len(nums)
        k = 0
        i = 0
        while i < nums_len:
            if nums[k] == val:
                nums.append(nums[k])
                del nums[k]
            else:
                k+=1
            i+=1
        return k
        
#https://leetcode.com/problems/remove-element?envType=problem-list-v2&envId=nz1q6a0h