import sys 
import markdown
input= sys.stdin.readline
N = int(input())
expression = input().strip()
numbers = []
# thx by (https://animoto1.tistory.com/entry/%EB%B0%B1%EC%A4%80-1935-%ED%9B%84%EC%9C%84-%ED%91%9C%EA%B8%B0%EC%8B%9D2-%ED%8C%8C%EC%9D%B4%EC%8D%AC-Python)
# 내가한거 1도없음
for _ in range(N):
    numbers.append(int(input()))

stack = []                    # stack 리스트를 통해 후위표기식 계산


for i in expression:
    
    if 'A' <= i <= 'Z' :
        
        stack.append(numbers[ord(i)-ord('A')]) # 이부분은 진짜 큰도움 $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    else:
        
        st2 = stack.pop()
        
        st1 = stack.pop()
        
        if i == '+' :
            stack.append(st1+st2)
            
        elif i == '-' :
            stack.append(st1-st2)
            
        elif i == '*' :
            stack.append(st1*st2)
            
        elif i == '/' :
            stack.append(st1/st2)
            
    

        
        

print('%.2f' %stack[0])




