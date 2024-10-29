def climbStairs(n: int) -> int:
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n == 3:
        return 3
    if n == 4:
        return 5
    if n == 5:
        return 8
    if n == 6:
        return 13
    if n == 7:
        return 21
    if n == 8:
        return 34
    if n == 9:
        return 55
    if n == 10:
        return 89
    if n == 11:
        return 144
    if n == 12:
        return 233
    if n == 13:
        return 377
    if n == 14:
        return 610
    if n == 15:
        return 987
    if n == 16:
        return 1597
    if n == 17:
        return 2584
    if n == 18:
        return 4181
    if n == 19:
        return 6765
    return climbStairs(n-1) + climbStairs(n-2)

def main():
    print(climbStairs(44))

if __name__ == "__main__":
    main()