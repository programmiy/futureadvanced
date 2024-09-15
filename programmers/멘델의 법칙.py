
'''
https://school.programmers.co.kr/learn/courses/15008/lessons/121685

일종의 브루트포스 문제
이해 명확히 안됨 
이전세대의 부모의 세대를 n-1세대라고 하면
구할려는 완두콩의 위치는 그 아래에 위치 할 수 밖에 없다.
RR - Rr - Rr - rr 의 계보는 그아래로 4^(n-1) 배수를 거치므로 4로 나눈 나머지로 계산한다.
한세대가 지날수록 그 아래 모든 집합은 그 전세대에 4를 곱한 배수로 늘어남 
'''


def solution(queries):
    answer = []
    for natural, position in queries:
        parent = "Rr"
        gener_code = []
        
        position-=1 # 0부터 시작하도록
        for i in range(natural-1):
            gener_code.append(position%4) # 0,1,2,3 중 하나
            position //= 4
           # print(f"position: {position}")

        print(f"gener_code: {gener_code}")
        while gener_code:
            position_by_generation = gener_code.pop()
            
            if parent == "Rr":
                if position_by_generation == 0:
                    parent = "RR"
                elif position_by_generation == 1 or  position_by_generation == 2:
                    parent = "Rr" 
                elif position_by_generation == 3:
                    parent = "rr"
            else: 
                break;
                
        answer.append(parent)
    return answer    
queries =[[3, 8], [2, 2]]
print(solution(queries))
