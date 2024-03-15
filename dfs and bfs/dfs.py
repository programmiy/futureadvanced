"""
DFS(Depth-First Search)
"""
myGraph = {
    'A': ['B', 'C', 'D'],
    'B': ['A', 'E'],
    'C': ['A', 'F', 'G'],
    'D': ['A', 'H'],
    'E': ['B', 'I'],
    'F': ['C', 'J'],
    'G': ['C'],
    'H': ['D'],
    'I': ['E'],
    'J': ['F']
}
def my_dfs(graph, start_node):
    visited = list() # 방문한 노드를 담을 배열
    stack = list() # 정점과 인접한 방문 예정인 노드를 담을 배열

    stack.append(start_node) # 처음에는 시작 노드 담아주고 시작하기.
    print(f"Stack: {stack}\n")
    while stack: # 더 이상 방문할 노드가 없을 때까지.
        node = stack.pop() # 방문할 노드를 앞에서 부터 하나싹 꺼내기.
        print(f"Pop: {node}")
        print(f"Stack after pop: {stack}\n")
        if node not in visited: # 방문한 노드가 아니라면
            visited.append(node) # visited 배열에 추가
            # stack.extend(graph[node]) # 해당 노드의 자식 노드로 추가
            print(f"Visited nodes: {visited}")
            print(f"Stack before extending: {stack}")
            stack.extend(reversed(graph[node]))
            print(f"Stack after extending: {stack}\n")
            

    print("dfs - ", visited)
    return visited
    
# 함수 실행
my_dfs(myGraph, 'A')
# dfs -  ['A', 'B', 'E', 'I', 'C', 'F', 'J', 'G', 'D', 'H’]
