# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def main_sum(self, root):
        if not root:
            return 0
        
        return root.val + self.main_sum(root.left) + self.main_sum(root.right)
    def findTilt(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        return abs(self.main_sum(root.left) - self.main_sum(root.right)) + self.findTilt(root.left) + self.findTilt(root.right)