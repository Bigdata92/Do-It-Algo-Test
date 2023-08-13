# 2750
import sys

input = sys.stdin.readline

num = int(input())

list1 = [int(input()) for _ in range(num)]
list2 = sorted(list1)

for _num in list2:
    print(_num)

