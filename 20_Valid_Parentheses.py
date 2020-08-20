class Solution:
    def isValid(self, s: str) -> bool:
        if s == '':
            return True
        stack = []
        for bracket in s:
            if bracket == '(' or bracket == '[' or bracket == '{' :
                stack.append(bracket)
            if bracket == ')':
                if len(stack) == 0 or stack[-1] != '(' :
                    return False
                else:
                    stack.pop()
            if bracket == ']':
                if len(stack) == 0 or stack[-1] != '[' :
                    return False
                else:
                    stack.pop()
            if bracket == '}':
                if len(stack) == 0 or stack[-1] != '{' :
                    return False
                else:
                    stack.pop()
        if len(stack) != 0:
            return False
        return True
            
