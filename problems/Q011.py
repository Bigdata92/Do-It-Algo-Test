# 1874
from collections import deque
import sys

input = sys.stdin.readline

n = int(input())

start_list = [i for i in range(1, n+1)]
tmp_list = deque()
result_list = []

for _ in range(n):
    target = int(input())

    if target in tmp_list:
        tmp_list.pop()
        result_list.append("-")

    for start in start_list:
        if start < target:
            start_list.remove(start)
            tmp_list.append(start)
            result_list.append("+")

        elif start == target:
            start_list.remove(start)
            tmp_list.append(start)
            result_list.append("+")

            tmp_list.pop()
            result_list.append("-")

        elif start > target:
            break

        print(start_list, "start_list")
        print(tmp_list, "tmp_list")
        print(result_list, "result_list")

    print(result_list, "result_list")
