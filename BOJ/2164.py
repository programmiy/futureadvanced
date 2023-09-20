from collections import deque
N = int(input())
dq = deque()
for i in range(1, N+1):
    dq.append(i)

for _ in range(len(dq)):
    
    if len(dq) ==1:
        print(dq.pop())
        break
    else:
        dq.popleft()
        dq.append(dq.popleft())