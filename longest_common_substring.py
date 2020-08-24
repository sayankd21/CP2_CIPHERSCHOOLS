s1 = 'geeksforgeeks'
s2 = 'geeksquiz'
result = 0
dp = [[0 for _ in range(len(s2)+1)] for _ in range(len(s1)+1)]
for i in range(len(s1)+1):
    for j in range(len(s2)+1):
        if (i == 0 or j == 0): 
            dp[i][j] = 0
        if s1[i-1] == s2[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
            result = max(result, dp[i][j])
        else:
            dp[i][j] = 0
print(result)
            
            
