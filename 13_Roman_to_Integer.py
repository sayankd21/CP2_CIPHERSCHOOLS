class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        num = 0
        i = 0
        j = len(s)
        while i < j:
            if i == j - 1:
                if s[i] == 'M':
                    num += 1000
                if s[i] == 'D':
                    num += 500
                if s[i] == 'C':
                    num += 100
                if s[i] == 'L':
                    num += 50
                if s[i] == 'X':
                    num += 10
                if s[i] == 'V':
                    num += 5
                if s[i] == 'I':
                    num += 1
                i += 1
                continue
            if s[i] == 'M':
                num += 1000
            elif s[i] == 'D':
                num += 500
            elif s[i] == "C":
                if s[i+1] == 'D': 
                    num += 400
                    i += 2
                    continue
                elif s[i+1] == 'M':
                    num += 900
                    i += 2
                    continue   
                else:
                    num += 100
            elif s[i] == 'L':
                num += 50
            elif s[i] == 'X':
                if s[i+1] == 'L': 
                    num += 40
                    i += 2
                    continue
                elif s[i+1] == 'C':
                    num += 90
                    i += 2
                    continue 
                else:
                    num += 10
            elif s[i] == 'V':
                num += 5
            else:
                if s[i+1] == 'V': 
                    num += 4
                    i += 2
                    continue
                elif s[i+1] == 'X':
                    num += 9
                    i += 2
                    continue
                else:
                    num += 1
            i += 1
        return num
                
                    
                
