#
def groupAnagrams(strs: list[str]) -> list[list[str]]:
    d = {}
    for s in strs:
        key = ''.join(sorted(s))
        if key in d:
            d[key].append(s)
        else:
            d[key] = [s]
    return list(d.values())