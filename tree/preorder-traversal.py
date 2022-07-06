from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        leftList = []
        rightList = []
        # 先处理根节点
        rootList = [root.val]
        # 递归处理左子树
        if root.left:
            leftList = self.preorderTraversal(root.left)
            rootList.extend(leftList)
        # 递归处理右子树
        if root.right:
            rightList = self.preorderTraversal(root.right)
            rootList.extend(rightList)
        return rootList
