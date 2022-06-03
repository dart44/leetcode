from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next 



class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        empty_list = ListNode()
        merged_list = empty_list
        
        while list1 and list2:
            if list1.val < list2.val:
                merged_list.next = list1
                list1 = list1.next
            else:
                merged_list.next = list2
                list2 = list2.next
            merged_list = merged_list.next
        

        if list1:
            merged_list.next = list1
        elif list2:
            merged_list.next = list2
            
        return empty_list.next
        

def print_list(linked_list: Optional[ListNode]) -> list:
    list_values = []
    for node in linked_list:
        list_values.append(node.val)
  
# Test script
def main():
    l1 = [ListNode(1, 2), ListNode(2, 4), ListNode(4)]
    l2 = [ListNode(1, 3), ListNode(3, 4), ListNode(4)]
    
    res = Solution()
    
    print(print_list(res.mergeTwoLists(l1, l2)))

# Run test script if this file is not being imported
if __name__ == '__main__':
    main()