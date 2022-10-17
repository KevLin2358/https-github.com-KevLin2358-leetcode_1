# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root == None:
            return []
        
        result = []
        que = collections.deque([root])
        
        while que:
            que_len = len(que)
            level = []
            
            for i in range(que_len):
                current = que.popleft()
                level.append(current.val)
                
                if current.left:
                    que.append(current.left)
                    
                if current.right:
                    que.append(current.right)
                
            result.append(level)
            
        return result