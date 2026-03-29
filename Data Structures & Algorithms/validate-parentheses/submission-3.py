class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for char in s:
            if char in "([{":
                stack.append(char)
            else:
                if not stack:
                    return False
                last = stack.pop()

                if (char == ")") and (last != "("):
                    return False
                elif (char == "]") and (last != "["):
                    return False
                elif (char == "}") and (last != "{"):
                    return False
        
        if not stack:
            return True
        return False