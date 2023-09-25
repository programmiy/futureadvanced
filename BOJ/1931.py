import sys

input = sys.stdin.readline

N= int(input())
max_cnt = 1
meetings = []
# 알고리즘 책에 있는걸론 이해 안되서 머리가 아팠음 내 능력 0사용 
for _ in range(N):
    meetings.append(list(map(int, input().split())))
meetings.sort(key=lambda x: (x[1], x[0])) # 종료시간을 기준으로 정렬해서 빨리 끝나는 순서대로 정렬, 종료 시간이 같은 경우 시작 시간이 빠른 순서대로 정렬

                                                                        #     시작 시간이 빠른 순서대로 정렬하면 겹치지 않는 미팅을 선택할 수 있기 때문


def timetable(meetings):
    count = 0
    start = 0  # 12시 시작 12시 종료 같은 경우도 계산가능 VVV
    for meet in meetings: # 모든 미팅에 대해 시작시간이 끝나는 시간보다 크거나 같으면 카운트 +1
        if meet[0] >= start:
            start = meet[1] # 다음시작시간과 비교하기 위해서 start를 종료시각으로 갱신
            count += 1
    return count



max_cnt= max(timetable(meetings), max_cnt) # 모든 미팅에 대해 max 갱신, 근데 이거 없어도 될듯?


print(max_cnt)