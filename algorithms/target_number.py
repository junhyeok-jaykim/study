
""" 
root: index 0
1 -> +1, -1
2 -> +2, -2

# 어떤 리스트가 있을 때 시작점은 index 0로 

# -elem, +elem 을 생성한 후

# 다음 element의 -elem, +elem과 연산


child nodes가 2개

     +1                      -1
    +2              -2
  +3    -3          +3, -3
+4 -4  +4 -4

+1, +2, +3, +4
+1, +2, +3 / -4
+1, +2/ -3, +4
+1, +2 -3/  -4


child node = 다음 element의 +, - (항상 2개)
원하는 target number가 완성되면 break하면 안된다 (같은 숫자의 원소가 뒤에 짝수로 포함될 수 있는 경우)
모두 탐색해야한다.
-> bfs, dfs
-> dfs
방문노드와 함께 summation을 기억해줘야한다.
예: 0, 1, 2, 3, 4
    0, 1, 2 5, 6 -> 0,1,2 의 summation 재활용

recursive method
"""

def get_every_possible_paths_of_target_number(number_list, target_number):
    possible_paths = []
    visited = [False] * len(number_list)

    for idx, num in enumerate(number_list):
        # num = 1
        visited[idx] = True
        # childs = [+2, -2]
        if visited[idx]
        child_nodes = [num, -num]
        
    while child_nodes:


    return len(possible_paths)





