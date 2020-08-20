class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        lst = []
        top = max(candies)
        for candy in candies:
            if candy + extraCandies >= top:
                lst.append(True)
            else:
                lst.append(False)
        return lst
