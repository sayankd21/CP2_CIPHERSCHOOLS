class Solution:
    def fib(self, N: int) -> int:
        i = 2
        if N == 0:
            return 0
        elif N == 1:
            return 1
        pv = 0
        last = 1
        while i <= N:
            item = pv + last
            pv,last = last, item
            i += 1
        return item
