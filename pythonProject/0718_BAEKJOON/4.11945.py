# N, M 받기
N, M = map(int, input().split())

# 붕어빵 모양 반대로 출력하기
# N개의 줄
for i in range(N):
    # 붕어빵 모양 입력 받기
    V = input()
    # 모양 반대로 하기
    reverse_V = V[::-1]

    print(reverse_V)