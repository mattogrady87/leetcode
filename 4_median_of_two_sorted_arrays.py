# Take 2 sorted arrays (python lists)
# Find the median of the two sorted arrays

# If its an even number then the median is the sum of the 
# two middle numbers divided by 2 Eg;
# [1,2] [3,4] would be (2+3)2 = 2.5

#nums1 = [1,2]
#nums2 = [3,4]

nums1 = []
nums2 = [2,3]


class Solution():
    def findMedianSortedArrays(self, nums1, nums2):
        """Get the median of two seperated, sorted arrays"""
        nums1+=nums2
        
        nums1 = sorted(nums1)
        middle = self.find_middle(nums1)

        if type(middle) is int:
            return middle
        # If type is tuple (meaning even # of nums)
        else:
            return self.find_median_from_tuple(middle)

    
    def find_median_from_tuple(self, nums_tuple):
        """Get median of two numbers from a tuple"""
        return (nums_tuple[0] + nums_tuple[1]) / 2


    def find_middle(self, nums):
        """Return the middle number or middle 2 numbers"""
        middle = float(len(nums))/2

        # If even numer of nums
        if len(nums) % 2 == 0:
            return nums[int(middle)], nums[int(middle-1)]
        # If odd number of nums
        else:
            return nums[int(middle - .5)]

sln = Solution()

print(sln.findMedianSortedArrays(nums1, nums2))

