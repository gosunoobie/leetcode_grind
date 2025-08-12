class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        check = {
            ')' : '(',
            '}' : '{',
            ']' : '['
        }

        for c in s:
            if c in check:  # If it's a closing bracket
                if stack and stack[-1] == check[c]:  # Top matches the opening
                    stack.pop()
                else:
                    return False  # Mismatch or empty stack
            else:
                stack.append(c)  # It's an opening bracket, push it

        return not stack  # Valid only if stack is empty
