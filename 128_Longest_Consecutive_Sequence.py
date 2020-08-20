class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        curr = 0
        maxm = 0
        nums.sort()
        if len(nums) == 1:
            return 1
        if nums == []:
            return 0
        for i in range(0,len(nums)-1):
            if curr == 0:
                curr += 1
                maxm = max(curr,maxm)
            if nums[i] == nums[i+1] - 1:
                curr += 1
                maxm = max(curr, maxm)
            elif nums[i] == nums[i+1]:
                pass
            else:
                curr = 0
                
        return maxm
