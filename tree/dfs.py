# 处理
def handle(node: map):
    print(node['value'])

# 获取左子节点
def get_left(current_index: int, tree: list) -> map:
    try:
        left_index = 2 * current_index + 1
        return {'index': left_index, 'value': tree[left_index]}
    except IndexError:
        return None
    except Exception:
        raise Exception

# 获取右子节点
def get_right(index: int, tree: list) -> map:
    try:
        right_index = 2 * index + 2
        return {'index': right_index, 'value': tree[right_index]}
    except IndexError:
        return None
    except Exception:
        raise Exception




# 深度优先， 利用栈
def dfs(tree: list):
    stack = list()
    root_index = 0
    root_value = tree[root_index]
    root_node = {'value': root_value, 'index': root_index}
    dfs_search(root_node, stack, tree)

# 搜索, 如果节点存在子节点, 优先递归搜索子节点, 否则入栈, 确保最底深的节点优先处理
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




if __name__ == '__main__':
    tree = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    dfs(tree)
