""" 
https://programmers.co.kr/learn/courses/30/lessons/43163#
"""


# 바꿀 수 있는 단어 확인
# 단, 이전 단어로 돌아가지는 않는다.
# 1) 바꿀 수 있는 단어가 없는 경우 -> 종료
# 2) 바꿀 수 있는 단어가 하나인 경우 -> 변경
# 3) 바꿀 수 있는 단어가 두개 이상인 경우

# hit -> hot -> lot -> dot
#                   -> log -> cog
#            -> dot -> lot (위에 path와 동일)
#                   -> dog -> cog
#
# 어떤 tree 형태의 데이터가 있고, shortest path를 찾는 문제
#
# solution1. 변환할 수 있는 모든 path를 찾고 그 중에서 최소인 경우를 반환하는 방법


def find_possible_conversion_words(word, words):
    conversion_words = []
    for cand in words:
        num_same = 0
        for word_char, cand_char in zip(word, cand):
            if word_char == cand_char:
                num_same += 1
        if num_same == 2:
            conversion_words.append(cand)
    return conversion_words

def make_graph(root, words):
    graph = {}
    cache = {}  # TODO
    graph[root] = find_possible_conversion_words(root, words)
    for word in words:
        conversion_words = find_possible_conversion_words(word, words)
        graph[word] = conversion_words

    return graph

def _print_graph(graph):
    for k, v in graph.items():
        print(k, v, sep='\t')

def solution(begin, target, words):
    min_num_conversion = 0

    # transform list to graph data representation
    # TODO: runtime 에서 graph 생성 
    graph = make_graph(begin, words)
    _print_graph(graph)

    # shortest path를 찾기 위해서는 bfs를 활용하여
    # 각 child level의 노드를 방문하면서 target node에 해당하는 경우
    # 종료하면 그것이 최단 경로가 자연스럽게 성립한다.

    # visit node
    visited = []
    level = 0   # initial level
    visit_nodes = [(level, begin)]
    while visit_nodes:
        cur_level, child = visit_nodes.pop(0)  # breadth-first
        if child not in visited:
            # visit order
            visited.append(child)
            # add another child
            visit_nodes.extend([(cur_level+1, x) for x in graph[child]])
            if child == target:
                min_num_conversion = cur_level
                break

    print(f'visit order: {visited}')
    return min_num_conversion

begin = "hit"
target = "cog"
words = ["hot", "dot", "dog", "lot", "log", "cog"]
#words = ["hot", "dot", "dog", "lot", "log"]
print(f"\nMinimum Conversion Count: {solution(begin, target, words)}")


## [other solution]
# from collections import deque
# 
# 
# def get_adjacent(current, words):
#     for word in words:
#         if len(current) != len(word):
#             continue
# 
#         count = 0
#         for c, w in zip(current, word):
#             if c != w:
#                 count += 1
# 
#         if count == 1:
#             yield word
# 
# 
# def solution(begin, target, words):
#     dist = {begin: 0}
#     queue = deque([begin])
# 
#     while queue:
#         current = queue.popleft()
# 
#         for next_word in get_adjacent(current, words):
#             if next_word not in dist:
#                 dist[next_word] = dist[current] + 1
#                 queue.append(next_word)
# 
#     return dist.get(target, 0)