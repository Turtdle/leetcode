def wordPattern(pattern: str, s: str) -> bool:
    d = {}
    # pattern =
#"aaa"

    # s =
#"aa aa aa aa"

    # Output: False
    s = s.split()
    d = {}
    # create a dictionary to store the mapping of pattern to s
    # then check if the mapping is correct
    if len(pattern) != len(s):
        return False
    for i in range(len(pattern)):
        if pattern[i] not in d:
            if s[i] in d.values():
                return False
            d[pattern[i]] = s[i]
        else:
            if d[pattern[i]] != s[i]:
                return False
    return True