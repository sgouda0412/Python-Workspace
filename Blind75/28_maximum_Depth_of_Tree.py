# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional, TreeNode
from collections import deque
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        #if not root:
        #    return 0
        #return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

        if not root:
            return 0
        
        lvl = 0
        q = deque([root])
        while q:
            for _ in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                
            lvl += 1
        return lvl
    

        