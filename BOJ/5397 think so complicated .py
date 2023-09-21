import sys
from collections import deque
## 알고리즘 구현 실패

input = sys.stdin.readline
right_state = None
for _ in range(int(input())):
    L = input()
    stack = []
    left = deque()
    right = []
    index = 0
    str_list = []
    if "-" in L:
        for i in L:
            if i != "-":
                
                str_list.append(i)
            else:
                str_list.pop()
    L =''.join(str_list)
        
    for l in L:
        if l == '<' or l=='>':
            if l=='<':
                if stack:
                    left.append(stack.pop())
                    
                elif stack == None:
                    continue    
                    
            elif l=='>':
                if right_state:
                    continue
                else:
                    
                    right_state = stack[-1]
                index +=1
                pass
            else:
                if left != None and right == None:
                    stack.append(l)
                    for i in left.popleft():
                        stack.append(i)
                        print(stack)
                elif left == None and right != None:
                    last_index = stack[-1]
                    if (right_state + index) >=last_index:
                        stack.append(l)
                    elif (right_state + index) < last_index:
                        stack.insert((right_state + index), l)
                    index = 0
                
                elif left == None and right == None:
                    if len(left) > index:
                        stack.append(l)
                        left_temp = deque()
                        while len(left) == index:
                            left_temp.append(left.popleft())
                        stack.append(left_temp.popleft())
                        stack.append(left.popleft())
                    elif len(left) < index:
                        
                        while index ==len(left):
                            index -=1
                        stack.append(l)
                        for _ in range(len(left)):
                            stack.append(left.popleft())  
                    elif len(left) == index:
                        for _ in range(len(left)):
                            stack.append(left.popleft())            
                    index = 0
                
                
                elif  left==None and right == None:
                    stack.append(l)
                    index = 0
        else:
            stack.append(l)
    for i in stack:
        print(i, end='')