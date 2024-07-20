import sys

input = sys.stdin.readline

# 테스트 케이스의 개수
T = int(input())

for i in range(T):
    # 반복 횟수 R, 문자열 S
    R, S = map(str, input().split())
    # R 숫자형으로
    R = int(R)
    for j in range(len(S)):
        # print(j)
        # end = '' : 한줄로 나오기 위해 옆으로 붙이기
        print(S[j] * R, end = '')
    # 줄 바꿈
    print()

