def reversePrefix(word: str, ch: str) -> str:
    if ch not in word:
        return word
    else:
        idx = word.index(ch)
        return word[:idx+1][::-1] + word[idx+1:]