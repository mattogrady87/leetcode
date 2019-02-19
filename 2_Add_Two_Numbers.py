# Reverse L1 and L2.
# Amalgamate each digit of the reversed listNodes into two seperate numbers
# Return the sum of those two numbers

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

l1 = ListNode(2)
l1n2 = ListNode(4)
l1n3 = ListNode(3)

l1.next = l1n2
l1n2.next = l1n3

l2 = ListNode(5)
l2n2 = ListNode(6)
l2n3 = ListNode(4)

l2.next = l2n2
l2n2.next = l2n3

# 342 + 465 = 807
# return a listnode with 7->0->8

class Solution():
    def __init__(self):
        self.cur_node = None
    
    def add_node(self, data):
        new_node = ListNode(data)
        new_node.next = self.cur_node
        self.cur_node = new_node

    def addTwoNumbers(self, l1, l2):
        l1_list = self.get_rev_num_from_list(l1)
        l2_list = self.get_rev_num_from_list(l2)
        nums = self.convert_and_add_nums(l1_list, l2_list)
        self.create_return_list(nums)
        return self.cur_node

    def print_list(self, list_to_print):
        head = list_to_print
        while(head != None):
            print(head.val)
            head = head.next

    def get_rev_num_from_list(self, list_to_parse):
        head = list_to_parse
        nums_str = ''
        while (head != None):
            nums_str += str(head.val)
            head = head.next
        return nums_str[::-1]
    
    def convert_and_add_nums(self, nums_str_1, nums_str_2):
        return int(nums_str_1) + int(nums_str_2)
    
    def create_return_list(self, list_to_parse):
        for x in list(str(list_to_parse)):
            self.add_node(int(x))



# Example driver code
    
sln = Solution()
asdf = sln.addTwoNumbers(l1, l2)
print(asdf.val)
print(asdf.next.val)
print(asdf.next.next.val)
