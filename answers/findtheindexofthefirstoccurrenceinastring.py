def strStr(haystack: str, needle: str) -> int:
    count = 0
    if needle == "":
        return 0
    for i, char in enumerate(haystack):
        #print(char, i)
        print(f'checking if {char} == {needle[count]}')
        print(f'count is {count}')
        print(f'i is {i}')
        if char == needle[count]:
            #print(char, needle[count])
            count += 1
            if count == len(needle):
                return i - count + 1
        else:
            print('resetting count')
            count = 0
    return -1


def main():
    print(strStr("mississippi", "issip"))

if __name__ == "__main__":
    main()