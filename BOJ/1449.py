n, L = map(int, input().split())
location = list(map(int, input().split()))

location.sort()  # 물이 새는 위치를 기준으로 정렬

count = 1  # 첫 번째 구간은 항상 테이프 1개로 막아야 함
last_tape = location[0] + L - 0.5  # 첫 번째 구간의 끝 위치, 여기서 무조건 시작해야함

for i in range(1, n):
    if location[i] + 0.5 <= last_tape:  # 현재 구간을 이전 테이프로 막을 수 있는 경우, 우측 0.5까지 붙일수 있기에 
        continue
    else:  # 새로운 테이프가 필요한 경우
        count += 1
        last_tape = location[i] + L - 0.5  # 새로운 테이프로 현재 구간을 막음

print(count)
# 책하고 알고리즘 다른데 맞음, power by copilot(내 코드 기반으로 개선된)


'''
문제에서는 "테이프를 자를 수 없고, 테이프를 겹쳐서 붙이는 것도 가능하다"고 명시되어 있습니다. 
따라서 한 번 사용한 테이프를 다시 사용하여 다른 구간을 막을 수 있습니다.

예를 들어, 테이프의 길이가 10이고, 물이 새는 위치가 [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]인 경우를 생각해보겠습니다. 
이 경우, 첫 번째 구간을 테이프 1개로 막은 후, 두 번째 구간을 테이프 1개로 막을 수 있습니다. 
이 때, 두 번째 구간의 시작 위치는 6이므로, 첫 번째 구간에서 사용한 테이프를 그대로 사용하여 두 번째 구간을 막을 수 있습니다.

따라서 한 번 사용한 테이프를 다시 사용하여 다른 구간을 막을 수 있으므로, 테이프를 모두 사용할 때까지 구간을 막을 수 있습니다.
'''
# >> 걍 문제를 또 잘못 이해함 ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ


##### 내 불완전한 코드, 나름 아무것도 안보고 품 

# import sys

# input = sys.stdin.readline

# cnt = 1
# n, l= map(int, input().split())
# location = list(map(int, input().split()))
# location.sort()
# def distance(n, location):
#     count = 1

#     if n ==0:
#         last_tape = 0
#         count += 1
#     else:
#         last_tape = n-0.5
#         count += 1
#     for locate in location: 
#         if last_tape != 0 and locate > last_tape +1:
             
#             count += 2
#         elif last_tape != 0 and locate == last_tape +1:
            
#             count += 1
#         last_tape = locate +0.5
#     return count

# cnt = distance(n, location)
# print(int((cnt*0.5)%3))
