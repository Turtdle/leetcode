def uncommonFromSentences(s1: str, s2: str) -> list[str]:
    words = s1.split() + s2.split()
    w = set()
    dupes= set()
    for word in words:
        if word in w:
            dupes.add(word)
        else:
            w.add(word)
    return list(w - dupes)