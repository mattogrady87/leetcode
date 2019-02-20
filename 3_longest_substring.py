# Receives a string as input
# Requires an int with longest substring without repeating characters
# Eg., the string 'abcddefg' would match 'abcd' which would want 4 returned

# new_count needs to be the number of new chars since the first occurence of the duplicate letter
# We should parse the watchstr_list to count how many and that's the new new_count, not 0, necessarily

# Delete the original occurence of the duplicate from the watchstr_list

class Solution():
    def lengthOfLongestSubstring(self, s):
        origstr_list = list(s)
        watchstr_list = []
        max_count = 0
        new_count = 0

        for x in origstr_list:
            if x in watchstr_list:
                if new_count > max_count:
                    max_count = new_count
                watchstr_list = watchstr_list[watchstr_list.index(x)+1:]
                new_count = len(watchstr_list)

            new_count+=1
            watchstr_list.append(x)

        if new_count > max_count:
            max_count = new_count
        return max_count

sln = Solution()


# expects 3
print(sln.lengthOfLongestSubstring('xxxxxxdvdf'))

# expects 1
print(sln.lengthOfLongestSubstring('bbbbbbbbb'))
# expects 3
print(sln.lengthOfLongestSubstring('abcabcbb'))
