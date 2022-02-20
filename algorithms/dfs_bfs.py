# stack = First-in Last-out (FILO) = `list`
# queue = First-in First-out (FIFO) = `deque` (from collections import deque)

# graph data representation 
# 1. adjacent matrix (memory-inefficient)
# 2. adjacent list (like 'linked list') (memory-efficient)

# DFS (Depth-first Search, 깊이우선탐색)
# root를 시작으로 child node를 우선적으로 방문하고 마지막 node를 방문한 후에는 다시 돌아와서 다음 child node를 방문하는 식으로 반복한다.
# 따라서 다시 돌아오기 위해서는 stack 자료구조를 사용한다.

""" Key Points
너비우선탐색(bfs)는 같은 level의 child를 먼저 방문하기 위해서 뒤에서 부터(next child) 제거
깊이우선탐색(dfs)는 next child 방문을 위해서 앞에서 부터 제거
"""

graph = {
    1: set([3, 4]),
    2: set([3, 4, 5]),
    3: set([1, 5]),
    4: set([1]),
    5: set([2, 6]),
    6: set([3, 5])
}
root = 1

def bfs(graph, root):
    """ 
    # 방문순서
    # init: root(1)
    # -> child: 3, 4
    # -> next child: (3부터) 1, 5, (4) 1
    # -> next next child: ...

    # 같은 레벨의 child list가 모두 없어지면(while) next child nodes로 이동
    """
    visited = []
    child_nodes = [root]
    while child_nodes:
        child = child_nodes.pop(0)
        if child not in visited:
            # 오른쪽으로 child nodes 삽입
            child_nodes += graph[child]
            visited.append(child)
    return visited

visited_order = bfs(graph, root)
print(visited_order)


def dfs(graph, root):
    """ 
    # 방문순서
    # init: root(1)
    # -> first child: 3
    # -> next child of first child: 1, 5 
    # -> 2

    # iteration의 종료는 leaf node에 도달할 때
    # 따라서
    """
    visited = []
    child_nodes = [root]
    while child_nodes:
        # NOTE: bfs와의 차이점(FILO, stack)
        # 깊이 우선을 위해서 child nodes에 들어간 노드 중에서도
        # 가장 최근 것부터 없애준다
        child = child_nodes.pop(-1)
        if child not in visited:
            # 오른쪽으로 child nodes 삽입
            child_nodes += graph[child]
            visited.append(child)
    return visited

visited_order = dfs(graph, root)
print(visited_order)


def dfs_recursive(graph, node, visited):
    for child in graph[node]:
        if child not in visited:
            visited.append(child)
            dfs_recursive(graph, child, visited)
    return visited

visited = [1]
visited_order = dfs_recursive(graph, 1, visited)
print(visited_order)
        
    