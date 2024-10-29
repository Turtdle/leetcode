def countBeautifulPairs(nums: list[int]) -> int:
    #is called beautiful if the first digit of nums[i] and the last digit of nums[j] are coprime.
    #coprime: gcd(a, b) == 1
    
    #this solution sucks
    def gcd(a: int, b: int) -> int:
        while b:
            a, b = b, a % b
        return a
    
    def isCoprime(a: int, b: int) -> bool:
        return gcd(a, b) == 1
    

    count = 0
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if isCoprime(int(str(nums[i])[0]), int(str(nums[j])[-1])):
                count += 1
    return count