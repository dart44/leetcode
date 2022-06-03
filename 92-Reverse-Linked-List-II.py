# Definition for singly-linked list.
import collections
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    prev = None
    while head:
        head.next, prev, head = prev, head, head.next
    return prev

class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if head and head.next == None:
            return head
        
        outer_left, outer_right, left_node, right_node = None, None, None, None
        
        index = 1
        while index < left-1:
            head = head.next
            index += 1
        
        outer_left = head
        head = head.next
        left_node = head
        # outer_left.next = None
        prev = None
        output = []
        
        while head and index < right:
            head.next, prev, head = prev, head, head.next
            index += 1
            if index == right:
                right_node = head
                outer_right = head.next
        
        left_node.next = outer_right
        outer_left.next = right_node
        
        
        return outer_left
        
        # queue = collections.deque()
        # queue.append(head)
        
        # while head and index <= right:
        #     queue.append(head)
        #     index += 1
        #     head = head.next
            
        
# # Test
# def main():
#     test = Solution()
#     n = 0
#     print(f'{test.name()}')
    
# # Run test script if this file is not being imported
# if __name__ == '__main__':
#     main()