def addDigits(num: int) -> int:
    while num >= 10:
        num = sum(getDigits(num))
    return num

def getDigits(num: int) -> List[int]:
    digits = []
    while num > 0:
        digits.append(num % 10)
        num //= 10
    return digits