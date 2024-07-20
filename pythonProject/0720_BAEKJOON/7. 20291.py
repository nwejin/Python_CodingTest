import sys
input = sys.stdin.readline

N = int(input())

# 타입과 횟수를 저장할 딕셔너리
a_dict= {}

for i in range(N):
    #파일명과 확장자를 공백제거후 .으로 나누어 입력 받음
    name, type = input().strip().split('.')
    # print(name, type)

    # 타입이 딕셔너리 안에 없으면 1 추가
    if type not in a_dict:
        a_dict[type] = 1
    else:
        # 존재하면 +1
        a_dict[type] += 1

# 딕셔너리를 사전순으로 정렬
sorted_dict = sorted(a_dict.items())

# 타입과 횟수 출력
for type, count in sorted_dict:
    print(type, count)

# print(a_dict)