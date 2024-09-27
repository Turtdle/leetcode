def reverse(x: int) -> int:
    y = int(str(x)[::-1]) if x >= 0 else -int(str(-x)[::-1])
    #if y is outside the range of a 32-bit signed integer, return 0
    return y if -(2**31) <= y <= 2**31 - 1 else 0
