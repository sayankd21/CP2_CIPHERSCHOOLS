class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        i = 0
        j = len(nums)
        count = 0
        while i < j:
            if nums[i] == 0:
                nums.pop(i)
                count += 1
                j -= 1
                i -= 1
            i += 1  
        for _ in range(count):
            nums.append(0)
        return nums
