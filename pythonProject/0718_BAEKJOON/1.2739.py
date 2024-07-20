# N 입력
N = int(input())

# 1~9까지 반복문
for i in range(1, 10):
    # f-string으로 출력
    print(f'{N} * {i} = {N*i}')