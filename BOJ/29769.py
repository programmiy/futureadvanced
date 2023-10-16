n = int(input())
a = list(map(int, input().split()))
q = int(input())


# 첫 번째 날에는 모든 학생들이 연주할 수 있음
selected = set(range(1, n+1))

for i in range(q):
    x, y = map(int, input().split())
    a[x-1] += y
    
    
    avg = sum(a[i-1] for i in selected) / len(selected)
    new_selected = set(i for i in selected if a[i-1] >= avg)

    # 평균이 같은 경우에는 학생 수가 많을수록, 학생 수가 같은 경우에는 가장 작은 번호를 가진 학생들을 선택함
    if len(new_selected) == len(selected):
        selected = new_selected
    elif len(new_selected) > len(selected):
        selected = new_selected
    else:
        selected = set(i for i in selected if a[i-1] > avg)
    
    # 선택된 학생들의 번호를 출력함
    print(*sorted(selected))