def divisorSubstrings( num: int, k: int) -> int:
    numstr = str(num)
    window = numstr[:k]
    result = 0
    for i in range(len(numstr)-k+1):
        if i > 0:
            window = window[1:] + numstr[i+k-1]
        
        if num % int(trin_zeros(window)) == 0:
            result += 1
    return result

#ez

def trim_zeros(numstr):
    while numstr[0] == '0':
        numstr = numstr[1:]
    return numstr
