# 풀이
# 1. 받은 토핑 크기 만큼
# 2. 토핑에서 수만큼 잘라서 각각 저장
# 3. 길이를 비교해서 동일한 경우 찾기

def solution(topping):
    answer = 0

    for i in range(1, len(topping)):
        a_set = set(topping[i:])
        b_set = set(topping[:i])

        if len(a_set) == len(b_set):
            answer += 1
    return answer


