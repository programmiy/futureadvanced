#https://school.programmers.co.kr/learn/courses/15008/lessons/121684
 # dfs 버전, 이렇게는 못풀거같은데 dfs개념을 확실하게 학습해야하는 문제
answer = 0
def DFS(L, s, ability, check):
    global answer
    n = len(ability)        # 학생 수
    m = len(ability[0])     # 종목 개수
    
    if L == m:
        print(f"Level: {L}, Sum: {s}, Check: {check}, Answer: {answer}")
        answer = max(answer, s)   # 능력치 합의 최댓값을 구함
        print(f"New Answer: {answer}")
    else:
        for i in range(n):
            if check[i] == 0:
                check[i] = 1
                print(f"Level: {L}, Sum: {s}, Check: {check}, Answer: {answer}")
                DFS(L+1, s + ability[i][L], ability, check)
                check[i] = 0
                print(f"Backtracking. Level: {L}, Sum: {s}, Check: {check}, Answer: {answer}")


def solution(ability):
    global answer
    check = [0]*len(ability)
    DFS(0, 0, ability, check)      
    # Level, sum, ability, check
    # L : level (고를 수 있는 학생 수 중 몇 명째 선택한 것인지), sum : 능력치의 합
    
    return answer

ability = [[40, 10, 10], [20, 5, 0], [30, 30, 30], [70, 0, 70], [100, 100, 100]]
print(solution(ability))