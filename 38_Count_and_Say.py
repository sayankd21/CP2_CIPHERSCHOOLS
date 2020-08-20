class Solution(object):
    def result(self, char):
        i = 0
        j = len(char)
        if j == 1:
            return '11'
        count = 1
        string = ''
        while i < j:
            if i == j - 1:
                string += str(count) + char[i]
                break
            if char[i] == char[i+1]:
                i += 1
                count += 1
            else:
                string += str(count) + char[i] 
                count = 1
                i += 1
        return string
            
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        entry = '1'
        for i in range(1,n):
            string = ''
            string = self.result(entry)
            entry = string
            
        return entry
