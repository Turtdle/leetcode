class Solution:
    def strWithout3a3b(self, a: int, b: int) -> str:
        outstring = ""
        last1 = ""
        last2 = ""
        while a != 0 or b != 0:
            if a == b:
                if last1 == 'a':
                    return outstring + 'ba' * a
                else:
                    return outstring + 'ab' * a
            if a > b:
                if not(last1 == 'a' and last2 == 'a'):
                    last2 = last1
                    outstring = outstring + "a"
                    a -= 1
                    last1 = "a"
                else:
                    last2 = last1
                    outstring = outstring + "b"
                    b -= 1
                    last1 = "b"
            else:
                if not(last1 == 'b' and last2 == 'b'):
                    last2 = last1
                    outstring = outstring + "b"
                    b -= 1
                    last1 = "b"
                else:
                    last2 = last1
                    outstring = outstring + "a"
                    a -= 1
                    last1 = "a"
        return outstring
