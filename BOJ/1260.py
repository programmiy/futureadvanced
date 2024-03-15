from collections import deque
#  powered by https://ji-gwang.tistory.com/291
def dfs(start):
    visited[start] = True
    print(start, end=' ')
    for i in graph[start]:
        if not visited[i]: # 방문하지 않았다면 재귀 recursion
            dfs(i)
            
def bfs(start):
    visited[start] = True
    queue = deque([start])
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if not visited[i]: #i를 방문해도 이 for문을 나간뒤에  while queue:에서 다시 graph[i]에 방문함 
                queue.append(i)
                visited[i] = True



N, M, V = map(int, input().split())
graph = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a) # 요 두개가 핵심

for i in graph:
    i.sort()

    
# DFS

visited = [False] * (N+1)
dfs(V)
print()

# BFS

visited = [False] * (N+1)
bfs(V)
