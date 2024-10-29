def longestPalindrome(s: str) -> str:
    def expand(s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left+1:right]
    res = ""
    for i in range(len(s)):
        s1 = expand(s, i, i)
        s2 = expand(s, i, i+1)
        res = max(res, s1, s2, key=len)
    return res
        