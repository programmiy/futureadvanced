N, K = map(int, input().split())

def josepus(N, K):
    remain = []
    temp = 0
    li = [i for i in range(1, N+1)]
    for _ in range(N):
        temp += K-1 #인덱스는 0부터 시작 1부터 K번째의 값 1+(k-1)
        print(temp)
        temp %= len(li) #temp 값을 전체 크기로 나눠줌으로써 k번째 수를 찾아줌
        print(temp, "2temp")
        remain.append(li.pop(temp)) # 제거
        print(remain, "remain")
        
        
            
            
    return remain
    
    
    
print(josepus(N, K))