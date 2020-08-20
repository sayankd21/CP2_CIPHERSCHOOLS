class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        lst = []
        for element in A:
            lst.append(element**2)
            
        return sorted(lst)
        
