import queue
from select import select
from typing import List


class Z_Heap:
    def __init__(self, nums: List[int]) -> None:
        self.__data = nums

    # 节点比较方法, 可重写, 相等返回0, 胜出返回1, 否则返回-1
    @classmethod
    def compare(cls, first: int, second: int):
        if first == second:
            return 0
        return 1 if first > second else -1

    @property
    def max_index(self):
        return len(self.__data) - 1

    @property
    def node_count(self):
        return len(self.__data)

    # 堆顶元素
    @property
    def best(self):
        return self.__data[0]

    # 获取左子节点index
    def get_left(self, index: int):
        return 2 * index + 1

    # 获取右子节点index
    def get_right(self, index: int):
        return 2 * index + 2

    # 获取父节点index
    def get_parent(self, index: int):
        if index == 0:
            return -1
        return int((index - 1)/2)

    # 从最后一个节点开始, 进行排序
    def heapify(self):
        if self.node_count < 2:
            return
        for i in reversed(range(self.node_count)):
            parent = self.get_parent(i)
            if parent != -1:
                self.sift_down(parent)

    # 取出堆顶节点(删除并返回)
    # 讲最小值(最大堆为例)与最大值交换, 弹出最大值, 然后对堆顶进行下沉操作
    def sift(self):
        if self.max_index == -1:
            raise Exception("empty heap")
        if self.max_index == 0:
            max = self.__data.pop()
            return max
        self.__data[0], self.__data[self.max_index] = self.__data[self.max_index], self.__data[0]
        max = self.__data.pop()
        self.sift_down(0)
        return max

    # 替换堆顶元素
    def replace(self, num):
        if self.node_count == 0:
            return
        replaced = self.__data[0]
        self.__data[0] = num
        self.sift_down(0)
        return replaced

    # 下沉
    # 先选出孩子节点中的较大值(最大堆为例), 然后与当前节点比较, 如果大于当前节点, 则交换位置, 并继续对被交换的孩子节点进行下沉
    def sift_down(self, index):
        node_val = self.__data[index]
        left_index = self.get_left(index)
        if left_index > self.max_index:
            return
        comparing_val = self.__data[left_index]
        comparing_index = left_index
        right_index = self.get_right(index)
        if right_index <= self.max_index:
            right_val = self.__data[right_index]
            if self.compare(right_val, comparing_val) == 1:
                comparing_val = right_val
                comparing_index = right_index
        if self.compare(comparing_val, node_val) == 1:
            self.__data[comparing_index], self.__data[index] = self.__data[index], self.__data[comparing_index]
            self.sift_down(comparing_index)

    # 上浮
    # 与父节点比较, 如果大于父节点(最大堆为例), 则交换位置, 并在新的位置上继续进行上浮操作
    def sift_up(self, index):
        node_val = self.__data[index]
        parent_index = self.get_parent(index)
        if parent_index != -1:
            parent_val = self.__data[parent_index]
            if self.compare(node_val, parent_val) == 1:
                self.__data[parent_index], self.__data[index] = self.__data[index], self.__data[parent_index]
                self.sift_up(parent_index)

    # 添加节点
    # 添加只队列末尾(堆的最远端), 然后进行上浮
    def push(self, num):
        self.__data.append(num)
        self.sift_up(self.max_index)

    # 打印堆
    def show(self):
        if self.max_index == -1:
            print("Heap is empty")
            return
        node_queue = queue.Queue()
        node_queue.put(0)
        print("+"*30)
        while not node_queue.empty():
            this_layer = self.get_layer(node_queue)
            print("+", end=" ")
            for idx in this_layer:
                print(self.__data[idx], end=" ")
                left_child = self.get_left(idx)
                right_child = self.get_right(idx)
                if left_child <= self.max_index:
                    node_queue.put(left_child)
                if right_child <= self.max_index:
                    node_queue.put(right_child)
            print("\n+")
        print("+"*30, "\n\n")

    # 从队列中取出当前层的所有节点
    def get_layer(self, queue):
        cur_all = []
        while not queue.empty():
            cur_all.append(queue.get())
        return cur_all


class A_Heap(Z_Heap):

    @classmethod
    def compare(cls, first: int, second: int):
        return super().compare(first, second) * -1


if __name__ == "__main__":
    z = A_Heap([1, 2, 3, 44, 55, 66, 77, 33, 20, 12, 19, 35, 36, 21])
    # sort
    z.heapify()

    print(">>max: ", z.best)
    z.show()
    # add
    z.push(21)
    print(">>max: ", z.best)
    z.show()

    for i in range(z.node_count):
        # remove
        print(">>removed max", z.sift())
        z.show()
