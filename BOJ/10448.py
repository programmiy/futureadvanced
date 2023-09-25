import sys

input = sys.stdin.readline
# copilot이 코파면서 짜준코드로 그냥 한번에 나옴 성능 ㅁㅊ놈임 걍 내가한건 1도없음
for _ in range(int(input())):
    n = int(input())
    for i in range(1, 46):
        for j in range(i, 46):
            for k in range(j, 46):
                if i * (i + 1) // 2 + j * (j + 1) // 2 + k * (k + 1) // 2 == n:
                    print(1)
                    break
            else:
                continue
            break
        else:
            continue
        break
    else:
        print(0)    