import sys

input = sys.stdin.readline

n, m = map(int, input().split())

li1 = []

for _ in range(n):
    li1.append(list(map(int, input().split())))

print(li1)

li1_sum = [[0] for _ in range(n+1)]
print(li1_sum)

for i in range(n):
    for j in range(n):
        li1_sum[i+1].append(li1_sum[i+1][-1] + li1[i][j])

print(li1_sum)
#
# for _ in range(m):
#     x1, y1, x2, y2 = map(int, input().split())
#     for idx in range(x1, x2+1):
#         print(li1_sum[idx - 1][y2] - li1_sum[idx - 1][y1 - 1])