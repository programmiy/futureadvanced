from itertools import combinations
# 조합 combinations
# 순서를 생각하는 배열 
arr = [x for x in range(4)]


for i in combinations(arr,2):
    print(i)
 

