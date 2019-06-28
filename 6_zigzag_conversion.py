class Solution():
    count = 0
    go_backwards = False

    def convert(self, s:str, numRows:int)->str:

        if numRows == 1:
            return s

        lists = [[] for i in range(0, numRows)]
        for x in s:
            lists[self.count].append(x)

            if not self.go_backwards:
                self.count += 1
            else:
                self.count -= 1
            if self.count == numRows-1:
                self.go_backwards = True
            if self.count == 0:
                self.go_backwards = False
        
        ret_str = "".join(str(r) for v in lists for r in v)
        return ret_str

sln = Solution()
print(sln.convert('PAYPALISHIRING', 4))
print(sln.convert('AB', 1))


# We save a letter from the given string in X different lists 
# So ('PAYPALISHIRING', 4) would create 4 different lists then go
# through the string so list[0] += P list[1] += A list[2] += Y, etc
# Then we concactenate them at the end.