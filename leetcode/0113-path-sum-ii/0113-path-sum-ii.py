# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        ans = []
        def dfs(root, arr, remaining):
            nonlocal ans
            if not root:
                return 
            arr.append(root.val)
            remaining -= root.val
            if not root.left and  not root.right and remaining == 0:
                ans.append(arr[:])
            dfs(root.left, arr, remaining)
            dfs(root.right, arr, remaining)

            arr.pop()
        dfs(root, [], targetSum)
        return ans
            