def lengthOfLongestSubstring(s: str) -> int:
    d = {}
    start = 0
    max_length = 0
    for i, c in enumerate(s):
        if c in d:
            start = max(start, d[c] + 1)
        d[c] = i
        max_length = max(max_length, i - start + 1)
    return max_length
            
