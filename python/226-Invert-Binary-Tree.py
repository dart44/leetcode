from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
# Insert Node
    def insert(self, val):
        if self.val:
            if val < self.val:
                if self.left is None:
                    self.left = TreeNode(val)
                else:
                    self.left.insert(val)
            elif val > self.val:
                if self.right is None:
                    self.right = TreeNode(val)
                else:
                    self.right.insert(val)
            else:
                self.val = val
# Print the Tree
    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print(self.val),
        if self.right:
            self.right.PrintTree()

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root == None: return root
        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root
        
# Test script
def main():
    input_value = TreeNode(2)
    input_value.insert(1)
    input_value.insert(3)
    res = Solution()
    print('Input')
    input_value.PrintTree()
    res.invertTree(input_value)
    print('Output')
    input_value.PrintTree()
    return

# Run test script if this file is not being imported
if __name__ == '__main__':
    main()