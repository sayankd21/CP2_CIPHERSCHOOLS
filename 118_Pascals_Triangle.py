class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if not numRows:
            return []

        num = [[] for _ in range(numRows)]
        num[0] = [1]
        if numRows==1:
            return [num[0]]
        
        num[1] = [1,1]
        if numRows==2:
            return [num[0],num[1]]
        
        num[2] = [1,2,1] 
        for i in range(3,numRows):
            num[i].append(1)
            for j in range(i-1):
                num[i].append(num[i-1][j]+num[i-1][j+1])
            num[i].append(1)
        return num
