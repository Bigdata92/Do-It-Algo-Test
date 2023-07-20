# Q1546

num = int(input())
list1 = list(map(int, input().split()))
print(list1)
print(max(list1))
tmp1 = max(list1)
list2 = [i/tmp1 * 100 for i in list1]
print(list2)
print(sum(list2) / len(list2))
