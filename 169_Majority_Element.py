class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        my_dict = {}
        for element in nums:
            if element not in my_dict:
                my_dict[element] = 0
            my_dict[element] += 1
        
        for key, value in my_dict.items():
            if value > int(len(nums)/2):
                return int(key)
