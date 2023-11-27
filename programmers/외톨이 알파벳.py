def solution(input_string):
    positions = {}
    for i, char in enumerate(input_string):
        if i > 0 and char == input_string[i - 1]:
            continue
        if char not in positions:
            positions[char] = []
        positions[char].append(i)
        print(f"positions after {i}-th iteration: {positions}")

    loners = []
    for char, pos in positions.items():
        if len(pos) > 1: #and pos[1] - pos[0] > 1:
            loners.append(char)
        print(f"loners after checking {char}: {loners}")

    if not loners:
        return "N"

    loners.sort()
    return "".join(loners)
print(solution("edeaaabbccd"))
#https://school.programmers.co.kr/learn/courses/15008/lessons/121683?language=python3