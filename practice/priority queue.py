from queue import PriorityQueue
#1. slow but safe
pq = PriorityQueue()

pq.put(123)
pq.put(456)
pq.put(789)

while not pq.empty():
    print(pq.get())


import heapq
#2.   fast but n-safe

