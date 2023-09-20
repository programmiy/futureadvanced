import sys, heapq
input = sys.stdin.readline
h = []
for _ in range(int(input())):
    
    i = int(input())
    if i ==0:
        print(heapq.heappop(h)[1] if len(h) else 0)
    else:
        heapq.heappush(h, (abs(i), i))


            
#책도움받음