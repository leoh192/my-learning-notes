# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None
        """
        :type val: int
        :type left: TreeNode or None
        :type right: TreeNode or None
        """
class Solution(object):
    
          
    def insert(self, root, val):
        
        if root.val:
            if val <= root.val:
                if root.left is None:
                    root.left = TreeNode(val)
                    return root.left
                else:
                    return Solution().insert(root.left,val)
            elif val > root.val:
                if root.right is None:
                    root.right = TreeNode(val)
                    return root.right
                else:
                    return Solution().insert(root.right,val)
        else:
            root.val = val
            return root

        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode(inserted node)
        """
    def delete(self, root, target):
        """
        :type root: TreeNode
        :type target: int
        :rtype: TreeNode(the root of new completed binary search tree) (cannot search())
        """
    def search(self,root,target):
        
        if root is None:
            return None
            
        if  root.val == target: 
            return root 
        
          elif root.val < target: 
                return Solution().search(root.right,val) 
    
        else: 
            return Solution().search(root.left,val)
        
            
        """
        :type root: TreeNode
        :type target: int
        :rtype: TreeNode(searched node)
        """
    def modify(self, root, target, new_val):
        """
        :type root: TreeNode
        :type target: int
        :type new_val: int
        :rtype:TreeNode(the root of new completed binary search tree) (cannot search())
