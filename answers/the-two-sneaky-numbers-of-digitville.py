def getSneakyNumbers(nums: list[int]) -> list[int]:
    """
    In the town of Digitville,
    there was a list of numbers called nums containing integers from 0 to n - 1.
    Each number was supposed to appear exactly once in the list,
    however,
    two mischievous numbers sneaked in an additional time,
    making the list longer than usual.

    As the town detective, your task is to find these two sneaky numbers.
    Return an array of size two containing the two numbers (in any order),
    so peace can return to Digitville.\
    """
    d = {}
    sneaky = []
    for num in nums:
        if num in d:
            d[num] += 1
            if d[num] == 2:
                sneaky.append(num)
        else:
            d[num] = 1
    return sneaky
