def plusOne(digits: list[int]) -> list[int]:
    strnum = ""
    for digit in digits:
        strnum += str(digit)
    num = int(strnum)
    num += 1
    new_digits = []
    for digit in str(num):
        new_digits.append(int(digit))
        