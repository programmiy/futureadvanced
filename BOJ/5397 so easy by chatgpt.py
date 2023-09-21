import sys
from collections import deque
# 직접 입력을 안하고 머리로만 생각해서 이런 간단한 알고리즘을 생각 못함 
input = sys.stdin.readline

for _ in range(int(input())):
    L = input().strip()
    stack = []
    left = deque()  
    index = 0

    for l in L:
        if l == '-':
            if stack:
                stack.pop()
        elif l == '<':
            if stack:
                left.appendleft(stack.pop())  # 후입선출 구조 이용 먼저들어온게 우측
        elif l == '>': #끝에선 커서 오른쪽으로 움직여도 의미없음
            if left:
                stack.append(left.popleft()) #후입선출 구조 이용 먼저들어온게 나중에 나가는게 당연함 
        else:                                   ## BP<<A의 경우 left = [B, P]에서 P가 나중에 나감 결과 ABP
            stack.append(l)

    stack.extend(left)
    print(''.join(stack))