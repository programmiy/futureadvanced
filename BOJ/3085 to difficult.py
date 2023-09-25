import sys

input = sys.stdin.readline
# 하나도 모르겠어서 인터넷 참고함 

# [링크](https://velog.io/@rhdmstj17/%EB%B0%B1%EC%A4%80-3085%EB%B2%88-%EC%82%AC%ED%83%95-%EA%B2%8C%EC%9E%84-python-%EB%B8%8C%EB%A3%A8%ED%8A%B8%ED%8F%AC%EC%8A%A4)
max_candy = 1
n = int(input())
board    = [list(input()) for _ in range(n)]

# 문제 자체가  뒤지게 어렵긴하지만 브루트포스중에선 이보다 더 좋은 문제를 찾기 힘들듯 
def fimax():
    max_cnt = 1
    for i in range(n):
        cnt =1
        for j in range(1, n): # 3-1인 2로 체크가능
            
        
            if board[i][j] == board[i][j-1]:
                cnt += 1
            else:
                cnt = 1
            max_cnt = max(max_cnt, cnt)
        for j in range(1, n): # 아래와 같은이유로 3-1인 2로 체크가능 
            if board[j][i] == board[j-1][i]:
                cnt += 1
            else:
                cnt = 1
            max_cnt = max(max_cnt, cnt)
    return max_cnt

for i in range(n):
    for j in range(n-1): #전체 열에 대해서 오른쪽 칸과 아래칸과 바꾸기
        if j+1 <n and board[i][j] != board[i][j+1]:     # 오른쪽과 바꾸기, 2만 반복하는 이유는 3에대해선 2에서 이미 바꿔서 확인했기 때문, 행의 마지막임
            board[i][j], board[i][j+1] = board[i][j+1], board[i][j]
            max_candy = max(max_candy, fimax())   # 바꾼값으로 최대값 구하기, 오른쪽이나 아래와 같은 값이 있는지 확인할것 
            board[i][j], board[i][j+1] = board[i][j+1], board[i][j]
        if i+1 <n and board[i][j] != board[i+1][j]:    # 아래와 바꾸기, 2만 반복하는 이유는 3에대해선 2에서 이미 바꿔서 확인했기 때문, 열의 마지막임
            board[i][j], board[i+1][j] = board[i+1][j], board[i][j]
            max_candy = max(max_candy, fimax())  # 바꾼값으로 최대값 구하기, 오른쪽이나 아래와 같은 값이 있는지 확인할것
            board[i][j], board[i+1][j] = board[i+1][j], board[i][j]



print(max_candy)