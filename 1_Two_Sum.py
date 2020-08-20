class Solution:
    def twoSum(self, lst: List[int], target: int) -> List[int]:
        for i in range(len(lst)):
                for j in range(i+1, len(lst)):
                    if lst[i] + lst[j] == target:
                        return [i,j]
        
        
