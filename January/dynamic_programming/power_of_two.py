#  Q4. ​https://leetcode.com/problems/power-of-two/

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if(n <= 0):
            return False
        elif(n == 1):
            return True
        else:
            while(n > 2):
                if(n % 2 != 0):
                    return False
                n = n / 2
        return True