class Solution:
    def reverse(self, x:int)->int:
        if x < 0:
            y = str(x)
            y = y[1:]
            y = '-' + y[::-1]
            y = int(y)
            if y < -2147483647:
                return 0
            return int(y)
         
        y = str(x)
        y = int(y[::-1])
        if y > 2147483647:
            return 0
        return y


sln = Solution()

print(sln.reverse(8463847412))