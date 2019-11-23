class TreeNode(object):
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    
          
    def insert(self,root,val):
        
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
 
    def find_max(self,root):

        now = root
        while now.right:
            now = now.right
        return now
    
    def delete(self,root,target):

        if root is None:
            return root
        else:
            if target < root.val:
                root.left = Solution().delete(root.left,target)
                return root
            elif target > root.val:
                root.right = Solution().delete(root.right,target)
                return root
            else:
                # where root is a leaf node
                if root.left is None and root.right is None:
                    root = None
                    return root
                if root.right is None or root.left is None:
                    # when root is a left tree
                    if root.left:
                        root = root.left
                        return root
                    # when root is a right tree
                    else:
                        root = root.right
                        return root
                # when root is a binary search tree
                elif root.left and root.right:
                    root.val = Solution().find_max(root.left).val
                    root.left = Solution().delete(self,root.left, root.val)
            return root

    # print the outcome of the tree
    def preorder(self, root):
        if root is not None:
            print(root.val)
            self.preorder(root.left)
            self.preorder(root.right)

    def search(self,root,target):
        
        if root is None:
            return None
            
        if  root.val == target: 
            return root 
        
        elif root.val < target: 
                return Solution().search(root.right,val) 
    
        else: 
            return Solution().search(root.left,val)
        
            

    def modify(self, root, target, new_val):
        
        if root is None:
            root=TreeNode(new_val)
        else:
            Solution().delete(root,target)
            Solution().insert(root,new_val)
        return root
    
    
    
    參考資料
    
    https://stackoverflow.com/questions/58981899/no-return-from-the-deletion-function-of-binary-search-tree
    https://www.geeksforgeeks.org/binary-search-tree-set-2-delete/
    http://alrightchiu.github.io/SecondRound/binary-tree-traversalxun-fang.html
    http://cslibrary.stanford.edu/110/BinaryTrees.html#s1
