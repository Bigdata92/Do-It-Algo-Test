import sys

input = sys.stdin.readline

n, m = map(int, input().split())
li1 = list(map(int, input().split()))

sum_li1 = [0]

for x in li1:
    sum_li1.append(sum_li1[-1] + x)

for _ in range(m):
    i, j = map(int, input().split())
    print(sum_li1[j] - sum_li1[i-1])