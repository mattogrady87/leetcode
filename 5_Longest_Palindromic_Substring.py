
# Find the longest palindromic substring in a string
# That is, the longest substring that is spelled the same way forwards
# As it is backwards.

# Eg., "babad" returns "bab"

class Solution():
    def __init__(self):
        self.substring = ''
        self.max = 0
        self.i = 0

    def longestPalindrome(self, s):
        self.s = s
        self.len = len(s)

        while self.i < self.len:
            self.lookahead()
        return self.substring


    def lookahead(self):
        for i in range(self.i,self.len):
            if self.s[self.i:i+1] == self.s[self.i:i+1][::-1]:
                if (i+1 - self.i) > self.max:
                    self.substring = self.s[self.i:i+1]
                    self.max = (i+1 - self.i)
        self.i+=1
        

sln = Solution()
print(sln.longestPalindrome('racecar'))

    

