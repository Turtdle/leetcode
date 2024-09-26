def isValid( s: str) -> bool:
    d = {'(' : 0, ')' : 0, '{' : 0, '}' : 0, '[' : 0, ']' : 0}
    for c in s:
        d[c] += 1
    print(d)
    return d['('] == d[')'] and d['{'] == d['}'] and d['['] == d[']'] and d['('] % 2 == 0 and d['{'] % 2 == 0 and d['['] % 2 == 0 and d[')'] % 2 == 0 and d['}'] % 2 == 0 and d[']'] % 2 == 0

def main():
    print(isValid("()"))
    # Output: True
    print(isValid("()[]{}"))
    # Output: True
    print(isValid("(]"))
    # Output: False
    print(isValid("([)]"))
    # Output: False
    print(isValid("{[]}"))
    # Output: True

if __name__ == '__main__':
    main()