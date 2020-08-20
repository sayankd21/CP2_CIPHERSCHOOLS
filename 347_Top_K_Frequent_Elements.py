class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        my_dict = {}
        for element in nums:
            if element not in my_dict:
                my_dict[element] = 0
            my_dict[element] += 1
        nums = sorted(my_dict.keys(), key = lambda k: my_dict[k])
        return nums[-k:]
        
