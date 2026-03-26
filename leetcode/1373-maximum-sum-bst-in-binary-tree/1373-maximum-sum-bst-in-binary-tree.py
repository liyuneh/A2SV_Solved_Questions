# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        def dfs(root):
            if not root:
                return True, 0 , float("inf"), float('-inf')
            l_isBST, l_sum, l_min, l_max = dfs(root.left)
            r_isBST, r_sum, r_min, r_max = dfs(root.right)

            if l_isBST and r_isBST and l_max < root.val < r_min:
                cur_sum = l_sum +  r_sum + root.val
                self.ans = max(self.ans, cur_sum)

                return (True, cur_sum, min(l_min, root.val), max(r_max, root.val))
            return False, 0 ,0,0
        dfs(root)
        return self.ans 