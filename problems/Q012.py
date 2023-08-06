# 17298

import sys

input = sys.stdin.readline

n = int(input())
input_li = list(map(int, input().split()))

stack_li = []       # index 저장 list
res_li = [0] * n    # 결과 list

for idx1 in range(n):
    while stack_li and input_li[stack_li[-1]] < input_li[idx1]: # 오큰수 조건
        res_li[stack_li.pop()] = input_li[idx1] # res_li에 오큰수 update
    stack_li.append(idx1)

while stack_li: # 오큰수 존재x 원소들 -1 처리
    res_li[stack_li.pop()] = -1

print(' '.join(map(str, res_li)))


