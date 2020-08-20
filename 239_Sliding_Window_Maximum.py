class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        lst = []
        i = 0
        j = len(nums)
        while i < (j-k)+1:
            lst.append(max(nums[i:i+k]))
            i += 1
        return lst
