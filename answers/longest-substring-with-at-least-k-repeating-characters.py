def longestSubstring(self, s: str, k: int) -> int:
    if not s:
        return 0

    counter = Counter(s)

    for char, count in counter.items():
        if count < k:
            return max(self.longestSubstring(sub_s, k) for sub_s in s.split(char))

    return len(s)

    #elegant ahh solution