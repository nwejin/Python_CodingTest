
N = int(input())

answer = 0

while N >= 0:
    # N이 5로 나눠질 경우
    if N % 5 == 0:
        answer += (N // 5)
        break

    # 5로 나눠지지 않을 경우 -3을빼면서 1을 더한다
    N -= 3
    answer += 1
else:
    # N이 다 끝나면 종료
    answer = -1

print(answer)