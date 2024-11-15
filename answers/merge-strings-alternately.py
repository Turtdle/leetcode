class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        output = ""
        for i in range(len(word1) + len(word2)):
            if not word1 or not word2:
                return output + word1 + word2
            if i % 2 == 0:
                output = output + word1[0]
                word1 = word1[1:]
            else:
                output = output + word2[0]
                word2 = word2[1:]
        return output
