# 11047
from collections import deque
import sys

input = sys.stdin.readline

n, k = map(int, input().split())
input_li1 = []
input_cnt_li1 = [0] * (n+1)
for _ in range(n):
    input_val = int(input())
    input_li1.append(input_val)

input_li1.reverse()

for idx, val in enumerate(input_li1):
    if k >= val:
        num1, num2 = k // val, k % val
        input_cnt_li1[idx] = num1
        k -= num1 * val

print(sum(input_cnt_li1))