import sys

input = sys.stdin.readline

input_li = [int(str) for str in input()[:-1]]
print(''.join(map(str, sorted(input_li, reverse=True))))
