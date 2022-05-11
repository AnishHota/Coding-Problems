class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c in ('(','{','['):
                stack.append(c)
            elif not(stack):
                return False
            elif c is ')' and stack[-1] is '(':
                stack.pop()
            elif c is '}' and stack[-1] is '{':
                stack.pop()
            elif c is ']' and stack[-1] is '[':
                stack.pop()
            else:
                return False
        if stack:
            return False
        return True
