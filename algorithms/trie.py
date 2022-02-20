"""
https://albertauyeung.github.io/2020/06/15/python-trie.html/ 
"""

import json
from dataclasses import dataclass, field
from typing import Dict

words = ['was', 'wax', 'what', 'word', 'work', 'mine']


@dataclass
class TrieNode:
    def __init__(self, char):
        self.char = char
        self.childs = {}
        self.is_leaf = False
        #self.prefix = ''

    def __repr__(self):
        return f'char: {self.char}, childs: {self.childs}'


trie = TrieNode(char='root')  # trie data structure

def insert(word, trie):
    # insertion
    # 각 char(node)를 순서대로 tree data에서 체크하며 insert 여부를 결정함
    curr_node = trie

    for char in word:
        if char in curr_node.childs:
            # 다음 child로 이동
            curr_node = curr_node.childs[char]
        else:
            # childs에 추가
            curr_node.childs[char] = TrieNode(char=char)
            # 추가된 child로 이동
            curr_node = curr_node.childs[char]
    
    curr_node.is_leaf = True

    return trie

trie = insert('was', trie)
trie = insert('wax', trie)
trie = insert('what', trie)
trie = insert('whadd', trie)
trie = insert('whaten', trie)
trie = insert('word', trie)
trie = insert('where', trie)
#print(json.dumps(repr(trie), indent=4))

# search by prefix matching
query_word = 'wh'

has_result = True
curr_node = trie
prefix = ''
for char in query_word:
    if char in curr_node.childs:
        # next node
        curr_node = curr_node.childs[char]
        prefix += char
    else:
        print('! no matching word')
        has_result = False
        break

def traverse_dfs(node, prefix, paths):
    # 끝 노드에서 이전 노드 전체를 계속 기억한다.
    if node.is_leaf:
        paths.append(prefix)
    for child in node.childs.values():
        traverse_dfs(child, prefix + child.char, paths)

if has_result:
    # print(curr_node)
    print(curr_node.childs.values())
    paths = []
    traverse_dfs(curr_node, prefix, paths)
    print(paths)
    # traverse
    #for char, _ in curr_node.childs.items():
    #    print(f'{prefix}{char}')





#def make_trie_data(words):
#    # 기본 operation은 insert
#    # 1. 현재 레벨에서 매칭되는 node(char)가 있는지
#    # 2. 있다면 이동
#    #    없다면 new node로 insert
#    trie = {}
#    root = ''
#    trie[root] = {}
#
#    node = root
#
#    for word in words:
#        level_nodes = trie[node]
#        for char in word:
#            if char in level_nodes:
#                # next search node
#                level_nodes = level_nodes[char]
#            else:
#                # new node
#                level_nodes[char] = {}
#                # next search node
#                node = char
#                level_nodes = level_nodes[char]
#        node = root
#
#    print(json.dumps(trie, indent=4))
#
#make_trie_data(words)
    

words = ['was', 'wax', 'what', 'word', 'work', 'mine']


# insert
# 현재 level에 매칭되는 node가 있는 경우 -> 다음 child node로 이동
#                          없는 경우 -> node 추가 후 해당 node로 이동
# 반복..


# class TrieNode:
#     
#     def __init__(self, char):
#         self.char = char
#         self.childs = {}
#         self.is_leaf = False
# 
# 
# class Trie:
#     
#     def __init__(self):
#         # root node
#         self.root_node = TrieNode(char="root")
# 
#     def insert_data(self, word):
#         """ root node를 따라서 insert """
#         node = self.root_node
#         for char in word:
#             if char in node.childs:
#                 # move next child
#                 node = node.childs[char]
#             else:
#                 # insert
#                 node.childs[char] = TrieNode(char=char)
#                 node = node.childs[char]
#         node.is_leaf = True
# 
#     def autocomplete(self, query):
#         # 1. 우선 최대로 일치하는 prefix 노드까지 찾는다
#         # 2. 깊이 우선으로 탐색 (이전 노드 char 기억)
# 
#         # find start node
#         start_node = self.root_node
#         for char in query:
#             if char in start_node.childs:
#                 start_node = start_node.childs[char]
#             else:
#                 return []
# 
#         return self._traverse_by_dfs(start_node, prefix=start_node.char, candidates=[])
# 
#     def _traverse_by_dfs(self, curr_node, prefix, candidates):
#         """ 
#         깊이 우선적으로 탐색하되, 이전 노드(precedent)를 알고 있어야 한다.
#         """
#         if curr_node.is_leaf:
#             candidates.append(prefix)
# 
#         for child in curr_node.childs.values():
#             self._traverse_by_dfs(child, prefix+child.char, candidates)
# 
#         return candidates
# 
#     
#         
# 
# trie = Trie()
# trie.insert_data('was')
# trie.insert_data('when')
# print(trie.autocomplete('w'))




