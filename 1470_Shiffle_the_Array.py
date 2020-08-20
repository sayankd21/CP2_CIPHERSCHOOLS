class Solution:
    def shuffle(self, lst: List[int], n: int) -> List[int]:
        pos = 1
        for i in range(n-1):
            temp = lst[n+i]
            lst.pop(n+i)
            lst.insert(pos,temp)
            pos += 2 
        return lst
