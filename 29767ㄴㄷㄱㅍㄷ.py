import sys

lines = sys.stdin.read().strip().split("\n")
N, K = map(int, lines[0].split())
arr = list(map(int, lines[1].split()))

sum = 0
prefixSum = []

for i in range(N):
    sum += arr[i]
    prefixSum.append(sum)

prefixSum.sort(reverse=True)
result = sum(prefixSum[:K])
print(str(result))
