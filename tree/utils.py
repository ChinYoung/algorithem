from decimal import Clamped
from typing import List

# 树节点
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class TreeUtils:
    # 从 list 创建树
    @classmethod
    def createTree(cls, vals: List[int]):
        root = cls.createNode(0, vals)
        return root

    # 从 list 创建节点及其子节点
    @classmethod
    def createNode(cls, index, vals):
        try:
            val = vals[index]
            node = TreeNode(val)
            # 递归创建左树
            node.left = cls.createNode(2 * index + 1, vals)
            # 递归创建右树
            node.right = cls.createNode(2 * index + 2, vals)
            return node
        except IndexError:
            return None
