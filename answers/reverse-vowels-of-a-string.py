class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = 'aeiouAEIOU'
        d = {}
        for i, char in enumerate(s):
            if char in vowels:
                d[i] = char
        sl = list(s)
        indexes = list(d.keys())
        top = len(indexes)-1
        for i, index in enumerate(indexes):
            sl[index] = d[indexes[top]]
            top -=1
        return ''.join(sl)
