from queue import PriorityQueue

data = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
k = 5

# 최소 힙에 데이터 추가
min_heap = PriorityQueue()
for num in data:
    min_heap.put(num)

# 큰 값들을 꺼내어 버림
for _ in range(k):
    heapq.heappop(max_heap)

# 5번째로 큰 값을 얻음
fifth_largest = -heapq.heappop(max_heap)

print(fifth_largest)