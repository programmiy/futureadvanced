graph = [
    [],      # 0
    [2, 3],  # 1 
    [4, 5],  # 2
    [6],     # 3
    [2, 5],  # 4
    [2, 4],  # 5
    [3, 7],  # 6
    [6]      # 7
]
# 방문 정보를 기록하기 위한 리스트
visited = [False] * 8

def dfs(v):
    print(f'방문 initial point: {v}')
    # 방문 표시
    visited[v] = True
    print(f'방문 노드: {v}, 방문 현황: {visited}', end='\n')
    # 그래프를 순환하면서 인접 노드들을 방문
    for i in graph[v]:
        print(f'graph[{v}]: {graph[v]}')
        print(f'현재 노드: {v}, 인접 노드: {i}')
        # 만약 방문하지 않은 노드가 있다면
        if not visited[i]:
            print(f"visited[{i}]: 가 {visited[i]}이므로 방문 ")
            print(f'visited[{i}]: {visited[i]} -> True')
            
            
            print(f'방문: {i}')
            print(f'dfs({i}) ')
            # 탐색 시작
            dfs(i)


# 탐색 시작 노드 1을 넣어주며 dfs() 실행
dfs(1)



