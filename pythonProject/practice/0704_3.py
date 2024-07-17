
# enemy에서 순서대로 n 빼기
def solution(n,k,enemy):
    answer = 0
    now = n
    result = []

    # 각 라운드마다 남은 체력 계산
    for i in range(len(enemy)):
        now -= enemy[i]
        result.append(now)

    # 음수인 경우에 k번 만큼 양수로 변경
    count = 0 #바꿀 횟수
    for j in range(len(result)):
        if result[j] < 0 and count < k:
            result[j] = abs(result[j])
            count += 1 # 바꿀때마다 1씩 증가

    for l in result:
        if l >= 0:
            answer += 1

    return answer


print(solution(2,4,[3, 3, 3, 3]))


