# Q11660

import sys

input = sys.stdin.readline

n, m = map(int, input().split())

li1 = []

for _ in range(n):
    li1.append(list(map(int, input().split())))

li1_sum = [[0] for _ in range(n+1)]

for i in range(n):
    for j in range(n):
        li1_sum[i+1].append(li1_sum[i+1][-1] + li1[i][j])

sum1 = 0
sum2 = 0
for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    result = 0
    for idx1 in range(x1, x2+1):
        sum1 = li1_sum[idx1][y2]
        sum2 = li1_sum[idx1][y1-1]
        result += (sum1 - sum2)

    print(result)