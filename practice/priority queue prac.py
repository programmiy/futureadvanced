from queue import PriorityQueue
#1. slow but safe    max-hip
pq = PriorityQueue()

pq.put(123)
pq.put(456)
pq.put(789)

while not pq.empty():
    print(pq.get())


import heapq
#2.   fast but n-safe   min-heap

h = []

heapq.heappush(h ,123)


heapq.heappush(h ,456)


heapq.heappush(h ,789)
while len(h):
    print(heapq.heappop(h))



