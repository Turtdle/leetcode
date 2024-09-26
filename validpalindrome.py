def isPalindrome(s: str) -> bool:
    s = list(s)
    current = 0
    for char in s:
        if char.isalnum():
            s[current] = char.lower()
            current += 1
    s = s[:current]

    return s == s[::-1]
    
    