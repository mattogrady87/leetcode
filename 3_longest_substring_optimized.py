class Solution():
    def lengthOfLongestSubstring(self, s):
        index_dct = {}
        max_count = curr_count = start_index = 0
        for curr_index, ch in enumerate(s):
            if ch in index_dct and index_dct[ch] >= start_index:
                max_count = max(max_count, curr_count)
                curr_count = curr_index - index_dct[ch]
                start_index = index_dct[ch] + 1
            else:
                curr_count += 1
            index_dct[ch] = curr_index
        return max(max_count, curr_count)


sln = Solution()
print(sln.lengthOfLongestSubstring('dvdf'))


