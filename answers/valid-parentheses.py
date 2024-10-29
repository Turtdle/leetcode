def isValid( s: str) -> bool:
    stack = []
    for char in s:
        if char == '(' or char == '{' or char == '[':
            stack.append(char)
        else:
            if not stack:
                return False
            if char == ')' and stack[-1] == '(':
                stack.pop()
            elif char == '}' and stack[-1] == '{':
                stack.pop()
            elif char == ']' and stack[-1] == '[':
                stack.pop()
            else:
                return False
    return not stack
def isValidRecursive(s, open_paran):
    parans = {'(': ')', '{': '}', '[': ']'}
    if not s:
        return not open_paran
    if s[0] in parans:
        return isValidRecursive(s[1:], open_paran + [s[0]])
    if not open_paran:
        return False
    if parans[open_paran[-1]] == s[0]:
        return isValidRecursive(s[1:], open_paran[:-1])
    return False




