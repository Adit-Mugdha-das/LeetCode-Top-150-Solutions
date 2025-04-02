# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def f(l,r):
            if l>r:
                return None
            m=(l+r)//2
            return TreeNode(nums[m],f(l,m-1),f(m+1,r))
        return f(0,len(nums)-1)

'''SOLVED BY ADIT MUGDHA DAS'''