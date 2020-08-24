class Solution:
    def numSquares(self, n: int) -> int:
        dp = []
        dp.append(0)
        dp.append(1)
        for i in range(2,n+1):
            result = n
            for j in range(1,i):
                if j * j > i :
                    break
                result = min(dp[i-j*j], result)    
            dp.append(result + 1)
        return dp[-1]
