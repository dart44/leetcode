from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def get_length(head: Optional[ListNode]):
    if not head:
        return 0
    return 1 + get_length(head.next)

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        pass1, pass2 = head, head
        
        while pass2 and pass2.next:
            pass1 = pass1.next
            pass2 = pass2.next.next
            if pass1 == pass2:
                return True
        return False
        
        
# Test
def main():
    test = Solution()
    n = [3,2,0,-4]
    print(f'{test.hasCycle()}')
    
# Run test script if this file is not being imported
if __name__ == '__main__':
    main()