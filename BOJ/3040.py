from itertools import combinations

for i in combinations([int(input()) for _ in range(9)], 7): # 몰라서 책봄
    if sum(i) == 100:
        print(i)
        break #sort는 요구하지않았기에
    
    
# 아래로 해도 맞았음

# from itertools import combinations

# for i in combinations([int(input()) for _ in range(9)], 7): # 몰라서 책봄
#     if sum(i) == 100:
#         for j in sorted(i):
#             print(j)
#         break