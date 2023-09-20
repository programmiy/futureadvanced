from collections import deque

# 덱 >>>>>>큐, 스택, 덱 등 다양한 데이터 구조를 구현


dq = deque()

dq.append(123)
dq.append(456)
while len(dq):
    print(dq.popleft())

