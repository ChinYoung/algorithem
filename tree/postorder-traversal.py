# 后续编译二叉树
# 之所以叫后序编译, 因为根节点处理在后, 同理中序, 后序遍历分别是在中间处理根节点和在后处理根节点

from typing import List, Optional
from utils import *

class Solution:
    def postOrderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return
        # 先递归处理左子树
        if root.left:
            self.postOrderTraversal(root.left)
        # 再递归处理右子树
        if root.right:
            self.postOrderTraversal(root.right)
        # 最后处理根节点
        self.handleNode(root)

    def handleNode(self, node: TreeNode):
        print(node.val)

if __name__ == "__main__":
    tree = [1,2,3,4,5,6]
    root = TreeUtils.createTree(tree)
    print(root)
    s = Solution()
    s.postOrderTraversal(root)