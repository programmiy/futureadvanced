#최소힙을 써야하는 문제 
import sys
import heapq
input = sys.stdin.readline
N= int(input())
h = []
# 메모리 겨우 12mb지랄해서 자꾸 안받아줌시발새끼 40분동안 열심히 했으나 포기
for _ in range(N):
    
    num = input().split()
    
    for n in num:

        
        heapq.heappush(h, -int(n))



# N번째로 작은 값을 찾기 위해 N-1번 힙에서 요소를 제거
for _ in range(N - 1):
    heapq.heappop(h)

result = -heapq.heappop(h)
print(result)