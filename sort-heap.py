import queue
from select import select
from typing import List


class Z_Heap:
    def __init__(self, nums: List[int]) -> None:
        self.__data = nums
        self.max_index = len(nums) - 1

    def get_left(self, index:int):
        return 2 * index + 1

    def get_right(self, index:int):
        return 2 * index + 2

    def get_parent(self, index:int):
        if index == 0:
            return -1
        return int((index - 1)/2)

    def heapify(self):
        if len(self.__data) < 2:
            return
        last = len(self.__data) - 1
        for i in reversed(range(last)):
            parent = self.get_parent(i)
            if parent != -1:
                self.sift_down(parent)

    def sift(self):
        if self.max_index == -1:
            raise Exception("empty heap")
        if self.max_index == 0:
            max = self.__data.pop()
            self.max_index = -1
            return max
        self.__data[0], self.__data[self.max_index] = self.__data[self.max_index], self.__data[0]
        max = self.__data.pop()
        self.max_index = len(self.__data) - 1
        self.sift_down(0)
        return max

    # 下沉, 确保节点比父节点小
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
            if right_val > comparing_val:
                comparing_val = right_val
                comparing_index = right_index
        if comparing_val > node_val:
            self.__data[comparing_index], self.__data[index] = self.__data[index], self.__data[comparing_index]
            self.sift_down(comparing_index)

    def sift_up(self, index):
        node_val = self.__data[index]
        parent_index = self.get_parent(index)
        if parent_index != -1:
            parent_val = self.__data[parent_index]
            if node_val > parent_val:
                self.__data[parent_index], self.__data[index] = self.__data[index], self.__data[parent_index]
                self.sift_up(parent_index)

    def push(self, num):
        self.__data.append(num)
        self.max_index = len(self.__data) - 1
        self.sift_up(self.max_index)

    def get_max(self):
        return self.__data[0]

    def show(self):
        if self.max_index == -1:
            print("")
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
        print("+"*30)

    def get_layer(self, queue):
        cur_all = []
        while not queue.empty():
            cur_all.append(queue.get())
        return cur_all

if __name__ == "__main__":
    z = Z_Heap([1, 2, 3, 44, 55, 66, 77, 33, 20, 12, 19, 35, 36, 21])
    # sort
    z.heapify()

    print(">>max: ", z.get_max())
    z.show()
    # add
    z.push(21)
    print(">>max: ", z.get_max())
    z.show()

    # remove
    print(">>removed max", z.sift())
    z.show()
    # remove
    print(">>removed max", z.sift())
    z.show()
    # remove
    print(">>removed max", z.sift())
    z.show()
    # remove
    print(">>removed max", z.sift())
    z.show()
    # remove
    print(">>removed max", z.sift())
    z.show()
    # remove
    print(">>removed max", z.sift())
    z.show()
    # remove
    print(">>removed max", z.sift())
    z.show()
    # remove
    print(">>removed max", z.sift())
    z.show()
    # remove
    print(">>removed max", z.sift())
    z.show()
    # remove
    print(">>removed max", z.sift())
    z.show()
    # remove
    print(">>removed max", z.sift())
    z.show()
    # remove
    print(">>removed max", z.sift())
    z.show()
    # remove
    print(">>removed max", z.sift())
    z.show()
    # remove
    print(">>removed max", z.sift())
    z.show()
    # remove
    print(">>removed max", z.sift())
    z.show()
    # remove
    print(">>removed max", z.sift())
    z.show()


