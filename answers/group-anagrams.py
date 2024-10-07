#
def groupAnagrams(strs: list[str]) -> list[list[str]]:
    d = {}
    if len(strs) == 0:
        return []
    d[strs[0]] = [strs[0]]
    for i in range(1, len(strs)):
        for key in d.keys:
            if check_anagram(key, strs[i]):
                d[key].append(strs[i])
            else:
                d[strs[i]] = strs[i]
    return d.values()



def check_anagram(str: s, str: s2) -> bool:
    d1 = {}
    d2 = {}
    if len(d1) != len(d2):
        return False
    for char in list(s):
        if char not in list(s2):
            return False
    return True
    

#