class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        result = 0
        count = 0
        lst = []
        for letter in s:
            if letter not in lst:
                lst.append(letter)
                count += 1
                result = max(count, result)
            else:
                n = lst.index(letter)
                lst = lst[n+1:]
                lst.append(letter)
                count -= n
        return result
