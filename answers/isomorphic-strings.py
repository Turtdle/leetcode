def isIsomorphic(s: str, t: str) -> bool:
#okay so how we are gonna do this
#hashmap
#if char isnt in the map keys, create a new one and map it to the other char
#if char is in map keys, if map[key] isnt equal to other char we return false
#else return true

    if len(s) != len(t):
        return False
    mapping = {}
    for i in range(len(s)):
        if s[i] not in mapping:
            mapping[s[i]] = t[i]
        elif mapping[s[i]] != t[i]:
            return False
    mapping = {}
    for i in range(len(t)):
        if t[i] not in mapping:
            mapping[t[i]] = s[i]
        elif mapping[t[i]] != s[i]:
            return False
    return True