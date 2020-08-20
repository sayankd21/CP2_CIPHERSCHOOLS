class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        h = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }
		
        if len(digits) == 0:
            return []
        		
        firstDigit = digits[0]
        firstDigitCharacters = h[firstDigit]
		
        furtherCombinations = self.letterCombinations(digits[1:])
        result = []
		
        if len(furtherCombinations) == 0:
                furtherCombinations.append("")
                
        for ele in firstDigitCharacters:
            for char in furtherCombinations:
                result.append(ele + char)
        return result
