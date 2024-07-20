import sys

# N 입력 받기
N = int(sys.stdin.readline())

# 경우의 수
answer = 0

# i부터 하나씩 더하면서 N이 나오면 중단/ answer에 1 더하기
# 중단된 숫자 다음부터 다시 시작
# -> N 까지 반복

for i in range(1, N+1):
    # print(i)
    sum = 0
    for j in range(i, N+1):
        sum += j
        if sum == N:
            answer += 1
            break


print(answer)


# while N == (i += i):
#     # N이 5로 나눠질 경우
#     if N % 5 == 0:
#         answer += (N // 5)
#         break
#
#     # 5로 나눠지지 않을 경우 -3을빼면서 1을 더한다
#     N -= 3
#     answer += 1
# else:
#     # N이 다 끝나면 종료
#     answer = -1
