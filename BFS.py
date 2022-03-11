# 深度优先， 利用栈
def dfs(tree: list):
    stack = list()
    root_index = 0
    root_value = tree[root_index]
    root_node = {'value': root_value, 'index': root_index}
    dfs_search(root_node, stack, tree)


def dfs_search(current_node: map, stack: list, tree: list):
    left_node = get_left(current_node['index'], tree)
    if left_node:
        dfs_search(left_node, stack, tree)
        stack.append(left_node)
    right_node = get_right(current_node['index'], tree)
    if right_node:
        dfs_search(right_node, stack, tree)
        stack.append(right_node)
    stack.append(current_node)
    handle(current_node)


# 广度优先， 利用队列
def bfs(tree: list):
    queue = list()
    root_index = 0
    root_value = tree[root_index]
    root_node = {'value': root_value, 'index': root_index}
    queue.append(root_node)
    bfs_search(queue, tree)


def bfs_search(queue: list, tree: list):
    current_node = queue.pop(0)
    handle(current_node)
    new_queue = extend_children(current_node['index'], queue, tree)
    if len(new_queue):
        bfs_search(new_queue, tree)


# 处理
def handle(node: map):
    print(node['value'])


def extend_children(current_index: int, queue: list, tree: list):
    left_node = get_left(current_index, tree)
    right_ndoe = get_right(current_index, tree)
    if left_node:
        queue.append(left_node)
    if right_ndoe:
        queue.append(right_ndoe)
    return queue


def get_left(current_index: int, tree: list) -> map:
    try:
        left_index = 2 * current_index + 1
        return {'index': left_index, 'value': tree[left_index]}
    except IndexError:
        return None
    except Exception:
        raise Exception


def get_right(index: int, tree: list) -> map:
    try:
        right_index = 2 * index + 2
        return {'index': right_index, 'value': tree[right_index]}
    except IndexError:
        return None
    except Exception:
        raise Exception


if __name__ == '__main__':
    tree = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    bfs(tree)
    print('--------------------------------------------------')
    dfs(tree)
