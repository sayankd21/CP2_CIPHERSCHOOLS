class Solution(object):
    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0
        if n == 1 or n == 2:
            return 1
        prev1 = 0
        prev2 = 1
        prev3 = 1
        i = 2
        result = 0
        while i < n:
            temp = prev1 + prev2 + prev3
            prev1, prev2, prev3 = prev2, prev3, temp
            result = temp
            i += 1
        return result
