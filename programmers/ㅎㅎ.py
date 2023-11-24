def max_values(double_list):
    max_values_list = []  # 최대 값들을 저장할 리스트 생성
    for lst in double_list:  # 이중 리스트의 각 리스트에 대해 반복
        max_value = max(lst)  # 각 리스트에서 최대 값을 찾음
        max_values_list.append(max_value)  # 최대 값을 새로운 리스트에 추가
    return max_values_list  # 최대 값들의 리스트 반환

# 아 인덱스 0~2 까지 조져서 각 인덱스별 최고값만 구하면 되는거구나
print(max_values([[40, 10, 10], [20, 5, 0], [30, 30, 30], [70, 0, 70], [100, 100, 100]]))