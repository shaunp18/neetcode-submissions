class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        keys = {")" : "(", "]" : "[", "}" : "{"}

        for char in s:
            if char in keys:
                if len(stack) == 0:
                    return False
                if stack[-1] == keys.get(char, 0):
                    stack.pop()
                    continue
                else:
                    return False

            else:
                stack.append(char)
        if len(stack) == 0:
            return True
        else:
            return False
            
