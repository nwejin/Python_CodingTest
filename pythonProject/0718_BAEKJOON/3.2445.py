# 입력 5 / 별 : 1~5~1 / 공백 : 8-6-4-2-0-2-4-6-8
# 한줄에 10개씩 표현

N = int(input())

# 기본 출력
for i in range(1, N+1):
    print('*' * i + ' ' * (N * 2 - (i * 2)) + '*' * i)

# 역순 출력
for j in range(N-1, 0, -1):
    print('*' * j + ' ' * (N * 2 - (j * 2)) + '*' * j)

