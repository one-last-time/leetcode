class Solution:
    def isHappy(self, n: int) -> bool:
        step = 1
        while step<=1000:
            print(n)
            tmp = 0
            while n:
                tmp += (n%10) * (n%10)
                n //= 10
            n = tmp
            step += 1
        if n == 1:
            return True
        return False

Solution().isHappy(19)