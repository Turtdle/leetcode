def lengthOfLastWord(self, s: str) -> int:
    return len(s.strip().split(" ")[-1]) if s else 0