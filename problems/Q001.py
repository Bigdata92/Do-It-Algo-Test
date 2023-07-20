# Q11720

# 짧은 풀이
# num1 = int(input())
#
# list1 = list(map(int, input()))
# print(list1)
# print(sum(list1))

# 정석
num2 = int(input())

list2 = list(input())
print(list2)

sum = 0
for i in range(num2):
    sum += int(list2[i])
print(sum)