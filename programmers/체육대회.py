# https://school.programmers.co.kr/learn/courses/15008/lessons/121684
# 뭔가 많이 난해했던 문제, 순열 개념이 장착되어 있어야 풀 수 있었음
from itertools import permutations
def solution(ability):
    answer = 0
    
    p = list(permutations(ability, len(ability[0])))
    print(p)
    print("------------------")
    print("len(p): ", len(p))
    for i in range(len(p)):
        total = 0
        for j in range(len(p[i])):
            total += p[i][j][j]
            print("p[i][j][j]: ", p[i][j][j])
            print("total: ", total)
        print(i, "번째 total: ", total)
        answer = max(answer, total)
    
    return answer
    

ability = [[40, 10, 10], [20, 5, 0], [30, 30, 30], [70, 0, 70], [100, 100, 100]]
print(solution(ability))