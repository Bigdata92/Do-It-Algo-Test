import sys

input = sys.stdin.readline

n = int(input())
li1 = list(map(int, input().split()))
li1.sort()

sum_li = []
sum_li.append(li1[0])
for idx in range(1,n):
    sum_num = sum_li[idx-1] + li1[idx]
    sum_li.append(sum_num)
print(sum(sum_li))