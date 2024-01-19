from collections import deque
ix = 1
def debug_var(name, value):
    
    
    global ix
        
        
    
    
    
    print(f"{ix}번째 DEBUG: {name} = {value}")
    ix += 1
    
def dfs(start):
    debug_var("visited", visited)
    visited[start] = True
    debug_var(f"after visited   {start}", visited)
    print(start, end=' \n')
    for i in graph[start]:
        print(f"graph[{start}] 살펴보기", i)
        if not visited[i]:
            debug_var("recursion by", i)
            dfs(i)
            
def bfs(start):
    visited[start] = True
    debug_var("after visited", visited)
    queue = deque([start])
    while queue:
        debug_var("popleft() 이전의 queue", queue)
        v = queue.popleft()
        debug_var("v", v)
        print(v, end=' \n')
        print(f"graph[{v}] 살펴보기", graph[v])
        for i in graph[v]:
            
            debug_var("graph", graph)
            print(f"graph[{v}] 살펴보기", i)
            if visited[i]:
               print(f'{i}는 이미 방문했으므로 무시합니다.') 
               print(f'visited[{i}] = {visited[i]}')
            if not visited[i]:
                debug_var("append i", i)
                queue.append(i)
                visited[i] = True
                debug_var("append 이후의 queue", queue)
                debug_var(f"{i} 방문처리된 visited", visited)
                debug_var("graph", graph)

N, M, V = map(int, input().split())
debug_var("N, M, V", (N, M, V))
graph = [[] for _ in range(N+1)]
debug_var("graph", graph)

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    debug_var("graph", graph)

for i in graph:
    i.sort()
print("graph sort complete", graph)
# ix=1
# print()
# print()
# print("DFS")
# print()
# print()
# print()
# visited = [False] * (N+1)
# debug_var("visited", visited)
# dfs(V)
# print()

ix=1
print("BFS")
visited = [False] * (N+1)
debug_var("visited", visited)
bfs(V)