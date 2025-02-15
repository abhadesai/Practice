class Solution:
    def isValid(self, s: str) -> bool:

        #Inner paranthesis needs to be closed first

        stack = []

# Dictionary to map closing brackets to their respective opening brackets
        bracket_map = {"}":"{",
                        ")":"(",
                        "]":"["}
        
        for c in s:
            if c in bracket_map:
                if stack and stack[-1] == bracket_map[c]:
                    stack.pop()
                else:
                    return False  #stack is empty
            else:
                stack.append(c)
        
        return True if not stack else False