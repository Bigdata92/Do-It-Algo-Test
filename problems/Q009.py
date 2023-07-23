# 12891

import sys

input = sys.stdin.readline

# 입력값
s, p = map(int, input().split())
dna = input()
target_list = list(map(int, input().split()))


# 초기화
tmp_list = [0] * 4  # ACGT 개수 저장 list
result = 0  # 결과


# 첫 문자열 'ACGT' 각 갯수 확인
def set_initial_value(str1):
    global tmp_list

    for data in str1:
        if data == 'A':
            tmp_list[0] += 1
        elif data == 'C':
            tmp_list[1] += 1
        elif data == 'G':
            tmp_list[2] += 1
        elif data == 'T':
            tmp_list[3] += 1

# tmp_list 계산(str1 '+' or '-')
def cal_dna(data, str1):
    global tmp_list
    if str1 == "+":
        if data == 'A':
            tmp_list[0] += 1
        elif data == 'C':
            tmp_list[1] += 1
        elif data == 'G':
            tmp_list[2] += 1
        elif data == 'T':
            tmp_list[3] += 1
    else:
        if data == 'A':
            tmp_list[0] -= 1
        elif data == 'C':
            tmp_list[1] -= 1
        elif data == 'G':
            tmp_list[2] -= 1
        elif data == 'T':
            tmp_list[3] -= 1

# tmp_list가 target_list 만족 여부 check
def check_tmp_list():
    global result, tmp_list, target_list
    res = True
    for k in range(4):  # 1개라도 불만족시 false
        if tmp_list[k] < target_list[k]:
            res = False

    if res:     # 4개 모두(ACGT) 만족시 True
        result += 1

set_initial_value(dna[:p])  # 초깃값 tmp_list 설정
check_tmp_list()            # 초깃값 tmp_list target_list 만족 여부 체크

for idx in range(1, s-p+1):

    cal_dna(dna[idx - 1], "-")      # tmp_list 맨 앞의 data 제거
    cal_dna(dna[idx + p - 1], "+")  # tmp_list 맨 뒤의 data 추가

    check_tmp_list()                # tmp_list의 target_list 여부 체크

print(result)

