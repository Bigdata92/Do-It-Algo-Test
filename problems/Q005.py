# 10986
import sys

input = sys.stdin.readline

n, m = map(int, input().split())
li1 = list(map(int, input().split()))

pre_sum_list = [0] * (n+1)
result = 0

for i in range(n):
    pre_sum_list[i+1] = pre_sum_list[i] + li1[i]

print(pre_sum_list)

# 5 3
# 1 2 3 1 2